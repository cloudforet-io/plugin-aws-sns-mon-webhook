import logging
import requests
import hashlib
import json
from datetime import datetime
from spaceone.core.manager import BaseManager
from spaceone.monitoring.model.event_response_model import EventModel

_LOGGER = logging.getLogger(__name__)
_INTERVAL_IN_SECONDS = 600
_TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S'


class EventManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse(self, options, raw_data):
        default_parsed_data = []

        raw_data_type = raw_data.get('Type')

        if raw_data_type == 'SubscriptionConfirmation':
            subscribe_url = raw_data.get('SubscribeURL')
            r = requests.get(subscribe_url)
            _LOGGER.debug(f'[Confirm_URL: SubscribeURL] {subscribe_url}')
            _LOGGER.debug(f'[AWS SNS: Status]: {r.status_code}, {r.content}')
        else:

            # INSUFFICIENT_DATA, ALARM, OK
            """
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
            if 'Message' in raw_data:
                message = raw_data.get('Message', '{}')
                raw_message = self._get_json_message(message)
                raw_data = raw_message
            # _LOGGER.debug(f'[EventManager] parse raw_data : {raw_data}')
            triggered_data = raw_data.get('Trigger', {})
            dimensions = triggered_data.get('Dimensions', [])

            for dimension in dimensions:
                event_resource = self._get_resource_for_event(dimension, {}, triggered_data)
                event_vo = {
                    'event_key': self._get_event_key(raw_data, dimension.get('value')),
                    'event_type': self._get_event_type(raw_data),
                    'severity': self._get_severity(raw_data),
                    'resource': event_resource,
                    'description': raw_data.get('NewStateReason', ''),
                    'title': self._get_alarm_title(raw_data, dimension),
                    'rule': self._get_rule_for_event(raw_data),
                    'occurred_at': self._get_occurred_at(raw_data),
                    'additional_info': self._get_additional_info(raw_data)
                }

                _LOGGER.debug(f'[EventManager] parse Event : {event_vo}')

                event_result_model = EventModel(event_vo, strict=False)
                event_result_model.validate()
                event_result_model_native = event_result_model.to_native()
                default_parsed_data.append(event_result_model_native)

        return default_parsed_data

    @staticmethod
    def _get_occurred_at(raw_data):
        current_time = datetime.now()
        occurred_at = raw_data.get('StateChangeTime', current_time)
        parsed_occurred_at = None

        if isinstance(occurred_at, datetime):
            parsed_occurred_at = occurred_at
        else:
            timestamp_str = occurred_at.split('.')
            if '.' in occurred_at:
                occurred_at_seconds = occurred_at[:occurred_at.find('.')]
                date_object = datetime.strptime(occurred_at_seconds, _TIMESTAMP_FORMAT)
                parsed_occurred_at = date_object
            else:
                date_object = datetime.strptime(occurred_at, _TIMESTAMP_FORMAT)
                parsed_occurred_at = date_object

        _LOGGER.debug(f'[EventManager] _occurred_at : {parsed_occurred_at}')
        return parsed_occurred_at

    @staticmethod
    def _get_event_key(raw_data, instance_id):
        # account_id:instance_id:alarm_name:date_time
        account_id = raw_data.get('AWSAccountId')
        alarm_name = raw_data.get('AlarmName')
        occurred_at = raw_data.get('StateChangeTime') if raw_data.get('StateChangeTime') is not None else datetime.now()
        indexed_unique_key = None

        if isinstance(occurred_at, str):
            point_position = occurred_at.find('.')
            occurred_at_timestamp = occurred_at if point_position == -1 else occurred_at[:point_position]
            date_object = datetime.strptime(occurred_at_timestamp, _TIMESTAMP_FORMAT)
            indexed_unique_key = int(date_object.timestamp()) // 600 * 100

        else:
            occurred_at_timestamp = str(occurred_at.timestamp())
            indexed_unique_key = int(occurred_at_timestamp) // 600 * 100

        raw_event_key = f'{account_id}:{instance_id}:{alarm_name}:{indexed_unique_key}'
        hash_object = hashlib.md5(raw_event_key.encode())
        md5_hash = hash_object.hexdigest()

        return md5_hash

    @staticmethod
    def _get_rule_for_event(raw_data):
        rule = ''
        if 'Trigger' in raw_data:
            trigger = raw_data.get('Trigger', {})
            threshold = trigger.get('Threshold')

            if isinstance(threshold, int):
                threshold = str(threshold)

            if isinstance(threshold, float):
                threshold = str(threshold)

            rule = threshold if threshold is not None else trigger.get('MetricName')

        return rule

    @staticmethod
    def _get_resource_for_event(dimension, event_resource, triggered_data):
        if 'name' in dimension:
            event_resource.update({
                'name': dimension.get('name')
            })
        if 'value' in dimension:
            event_resource.update({
                'resource_id': dimension.get('value')
            })
        if 'Namespace' in triggered_data:
            event_resource.update({
                'resource_type': triggered_data.get('Namespace')
            })

        return event_resource

    @staticmethod
    def _get_alarm_title(raw_data, dimension):
        alarm_name = raw_data.get('AlarmName', '')
        value = dimension.get('value')
        return f'[{value}]: {alarm_name}'

    @staticmethod
    def _get_additional_info(raw_data):
        additional_info = {}
        if 'Trigger' in raw_data:
            pass
        if 'OldStateValue' in raw_data:
            additional_info.update({'old_state_value': raw_data.get('OldStateValue')})

        if 'AlarmName' in raw_data:
            additional_info.update({'alarm_name': raw_data.get('AlarmName')})

        if 'Region' in raw_data:
            additional_info.update({'region': raw_data.get('Region')})

        if 'AWSAccountId' in raw_data:
            additional_info.update({'aws_account_id': raw_data.get('AWSAccountId')})

        if 'AlarmDescription' in raw_data:
            additional_info.update({'alarm_description': raw_data.get('AlarmDescription')})

        if 'AlarmArn' in raw_data:
            additional_info.update({'alarm_arn': raw_data.get('AlarmArn')})

        return additional_info

    @staticmethod
    def _get_severity(raw_data):
        sns_event_state = raw_data.get('NewStateValue')
        default_severity_flag = 'NOT_AVAILABLE'
        if sns_event_state == 'OK':
            default_severity_flag = 'INFO'
        elif sns_event_state == 'ALERT':
            default_severity_flag = 'ERROR'

        return default_severity_flag

    @staticmethod
    def _get_event_type(raw_data):
        sns_event_state = raw_data.get('NewStateValue', 'INSUFFICIENT_DATA')
        return 'RECOVERY' if sns_event_state == 'OK' else 'ALERT'

    @staticmethod
    def _get_event_type(raw_data):
        sns_event_state = raw_data.get('NewStateValue', 'INSUFFICIENT_DATA')
        return 'RECOVERY' if sns_event_state == 'OK' else 'ALERT'

    @staticmethod
    def _get_json_message(json_raw_data):
        new_json = {}
        try:
            new_json = json.loads(json_raw_data)
        except Exception as e:
            _LOGGER.debug(f'[EventManager] _get_json_message : {json_raw_data}')
        return new_json
