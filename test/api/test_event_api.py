import logging
import unittest
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json
from pprint import pprint

_LOGGER = logging.getLogger(__name__)


class TestEvent(TestCase):
    def test_parse(self):
        options = {}
        raw_data = {
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

        parsed_data = self.monitoring.Event.parse({'options': options, 'data': raw_data})
        print_json(parsed_data)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
