import logging
import requests
import hashlib
import json
from datetime import datetime

from spaceone.core.manager import BaseManager
from spaceone.monitoring.model.event_response_model import EventModel
from spaceone.monitoring.error.event import *

_LOGGER = logging.getLogger(__name__)


class EventManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse(self, options, raw_data):
        try:
            if raw_data.get('Type') == 'SubscriptionConfirmation':
                self.request_subscription_confirm(raw_data.get('SubscribeURL'))
                return []
            else:
                """ --- RAW_DATA Sample ---
                "TopicArn": "arn:xxxxx",
                "Subject": "ALARM: ....",
                "SigningCertURL": "https://sns..../...pem",
                "MessageId": "838a70d8-d3c7-5d0c-a03a-29789bc46b66",
                "Message": "{RAW_JSON_MESSAGE}",
                "Timestamp": "2021-08-25T13:29:39.389Z",
                "SignatureVersion": "1",
                "Type": "Notification",
                "Signature": "ht4kn+........==",
                "UnsubscribeURL": "https://sns......"
                """
                return self._generate_events(self._get_json_message(raw_data.get('Message', {})), raw_data)

        except Exception as e:
            raise ERROR_PARSE_EVENT(field=e)

    def _generate_events(self, message, raw_data):
        events = []

        """ MESSAGE Sample1
            {
                "OldStateValue": "ALARM",
                "Trigger": {
                    "StatisticType": "Statistic",
                    "EvaluationPeriods": 1,
                    "Period": 300,
                    "MetricName": "CPUUtilization",
                    "Namespace": "AWS/EC2",
                    "TreatMissingData": "- TreatMissingData:                    missing",
                    "Statistic": "MAXIMUM",
                    "Unit": "None",
                    "EvaluateLowSampleCountPercentile": "",
                    "Dimensions": [
                        {
                            "value": "i-0b79aaf581d5389d5",
                            "name": "InstanceId"
                        }
                    ],
                    "ComparisonOperator": "GreaterThanThreshold",
                    "Threshold": 50.0
                },
                "AlarmName": "cpu corek8s ",
                "Region": "AsiaPacific (Seoul)",
                "AWSAccountId": "257706363616",
                "NewStateValue": "OK",
                "AlarmDescription": "cpucorek8s",
                "AlarmArn": "arn:aws:cloudwatch:ap-northeast-2:257706363616:alarm:cpucorek8s",
                "NewStateReason": "Threshold Crossed: 1 out of the last 1 datapoints [9.395 (10/06/21 04:23:00)] was not greater than the threshold (50.0) (minimum 1 datapoint for ALARM -> OK transition).",
                "StateChangeTime": "2021-06-10T04:28:46.868+0000"
            }
            acc_id > resource_id > alarm_name > date_time
        """

        """ MESSAGE Sample2
            {
                "AlarmName": "ContainerInsight-pod_cpu_utilization",
                "AlarmDescription": null,
                "AWSAccountId": "257706363616",
                "NewStateValue": "ALARM",
                "NewStateReason": "Thresholds Crossed: 1 out of the last 1 datapoints [0.3647359623208398 (25/08/21 13:28:00)] was less than the lower thresholds [0.3745361004392295] or greater than the upper thresholds [0.42329814009957095] (minimum 1 datapoint for OK -> ALARM transition).",
                "StateChangeTime": "2021-08-25T13:29:39.346+0000",
                "Region": "Asia Pacific (Seoul)",
                "AlarmArn": "arn:aws:cloudwatch:ap-northeast-2:257706363616:alarm:ContainerInsight-pod_cpu_utilization",
                "OldStateValue": "OK",
                "Trigger": {
                    "Period": 60,
                    "EvaluationPeriods": 1,
                    "ComparisonOperator": "LessThanLowerOrGreaterThanUpperThreshold",
                    "ThresholdMetricId": "ad1",
                    "TreatMissingData": "- TreatMissingData:                    missing",
                    "EvaluateLowSampleCountPercentile": "",
                    "Metrics": [{
                        "Id": "m1",
                        "MetricStat": {
                            "Metric": {
                                "Dimensions": [{
                                    "value": "cloudone-dev-v1-eks-cluster",
                                    "name": "ClusterName"
                                }],
                                "MetricName": "pod_cpu_utilization",
                                "Namespace": "ContainerInsights"
                            },
                            "Period": 60,
                            "Stat": "Average"
                        },
                        "ReturnData": true
                    },
                    {
                        "Expression": "ANOMALY_DETECTION_BAND(m1, 0.592)",
                        "Id": "ad1",
                        "Label": "pod_cpu_utilization (expected)",
                        "ReturnData": true
                    }]
                }
            }
        """

        triggered_data = message.get('Trigger', {})
        region = message.get('Region', '')
        occurred_at = self._get_occurred_at(message)
        namespace = self._get_namespace(message)

        for dimension in triggered_data.get('Dimensions', []):
            event_dict = self._generate_event_dict(message, dimension, triggered_data, namespace, region, occurred_at, raw_data)
            _LOGGER.debug(f'[EventManager] parse Event : {event_dict}')
            events.append(self._evaluate_parsing_data(event_dict))

        for metric in triggered_data.get('Metrics', []):
            metric_data = metric.get('MetricStat', {}).get('Metric', {})

            for dimension in metric_data.get('Dimensions', []):
                event_dict = self._generate_event_dict(message, dimension, triggered_data, namespace, region, occurred_at, raw_data)
                _LOGGER.debug(f'[EventManager] parse Event : {event_dict}')
                events.append(self._evaluate_parsing_data(event_dict))

        return events

    def _generate_event_dict(self, message, dimension, triggered_data, namespace, region, occurred_at, raw_data):
        return {
            'event_key': self._get_event_key(message, dimension.get('value'), occurred_at),
            'event_type': self._get_event_type(message),
            'severity': self._get_severity(message),
            'resource': self._get_resource_for_event(dimension, namespace, region),
            'description': message.get('NewStateReason', ''),
            'title': raw_data.get('Subject'),
            'rule': self._get_rule_for_event(message),
            'occurred_at': occurred_at,
            'additional_info': self._get_additional_info(message)
        }

    @staticmethod
    def _get_namespace(message):
        if ns := message.get('Trigger', {}).get('Namespace'):
            return ns
        else:
            for metric in message.get('Trigger', {}).get('Metrics', []):
                _m = metric.get('MetricStat', {}).get('Metric', {})
                if ns := _m.get('Namespace'):
                    return ns

        return ''

    @staticmethod
    def request_subscription_confirm(confirm_url):
        r = requests.get(confirm_url)
        _LOGGER.debug(f'[Confirm_URL: SubscribeURL] {confirm_url}')
        _LOGGER.debug(f'[AWS SNS: Status]: {r.status_code}, {r.content}')

    @staticmethod
    def _get_occurred_at(message):
        if t := message.get('StateChangeTime'):
            return datetime.strptime(t, '%Y-%m-%dT%H:%M:%S.%f+0000')
        else:
            return datetime.now()

    @staticmethod
    def _get_event_key(message, resource_id, occurred_at):
        """
        Generate the Index Key through Hashing
            {account_id}:{instance_id}:{alarm_name}:{date_time}
        """

        account_id = message.get('AWSAccountId')
        alarm_name = message.get('AlarmName')
        datetime_key = int(occurred_at.timestamp() // 600 * 100)

        raw_event_key = f'{account_id}:{resource_id}:{alarm_name}:{datetime_key}'
        hash_object = hashlib.md5(raw_event_key.encode())
        md5_hash = hash_object.hexdigest()

        return md5_hash

    @staticmethod
    def _get_rule_for_event(message):
        # TODO
        rule = ''

        return rule

    @staticmethod
    def _get_resource_for_event_from_metric(dimension, event_resource, triggered_data, region):
        resource_type = triggered_data.get('Namespace', '')
        resource_id = dimension.get('value', '')
        resource_name = ''
        if region != '':
            resource_name = f'[{region}]'
        if resource_type != '':
            resource_name = resource_name + f':[{resource_type}]'

        event_resource.update({
            'name': resource_name + f': {resource_id}',
            'resource_id': resource_id,
        })
        if resource_type != '':
            event_resource.update({
                'resource_type': resource_type
            })

        return event_resource

    @staticmethod
    def _get_resource_for_event(dimension, namespace, region):
        """
        dimension sample"
        {
            "value": "i-0b79aaf581d5389d5",
            "name": "InstanceId"
        }
        :return
        {
          resource_id,
          resource_type,
          name
        }
        """

        return {
            'resource_id': dimension.get('value', ''),
            'resource_type': namespace,
            'name': f'[{namespace}] {dimension.get("name", "")}={dimension.get("value", "")} ({region})'
        }

    @staticmethod
    def _get_additional_info(message):
        additional_info = {}
        additional_info_key = ['OldStateValue', 'AlarmName', 'Region', 'AWSAccountId', 'AlarmDescription', 'AlarmArn']

        for _key in message:
            if _key in additional_info_key and message.get(_key):
                additional_info.update({_key: message.get(_key)})

        return additional_info

    @staticmethod
    def _get_severity(message):
        """
        Severity:
            - CRITICAL
            - ERROR
            - WARNING
            - INFO
            - NOT_AVAILABLE
        """
        sns_event_state = message.get('NewStateValue')

        if sns_event_state == 'OK':
            severity_flag = 'INFO'
        elif sns_event_state in ['ALERT', 'ALARM']:
            severity_flag = 'ERROR'
        else:
            severity_flag = None

        return severity_flag

    @staticmethod
    def _get_event_type(message):
        sns_event_state = message.get('NewStateValue', 'INSUFFICIENT_DATA')
        return 'RECOVERY' if sns_event_state == 'OK' else 'ALERT'

    @staticmethod
    def _get_json_message(json_raw_data):
        return json.loads(json_raw_data)

    @staticmethod
    def _evaluate_parsing_data(event_data):
        event_result_model = EventModel(event_data, strict=False)
        event_result_model.validate()
        return event_result_model.to_native()