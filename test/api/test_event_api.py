import logging
import unittest
import os
import json
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json
from pprint import pprint

_LOGGER = logging.getLogger(__name__)


class TestEvent(TestCase):
    def test_parse(self):
        param = {
            "options": {

            },
            "data": {
                "SigningCertURL": "https://sns.ap-northeast-2.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",
                "Subject": "OK: \"ContainerInsight-pod_cpu_utilization\" in Asia Pacific (Seoul)",
                "SignatureVersion": "1",
                "TopicArn": "arn:aws:sns:ap-northeast-2:257706363616:spaceone-notification",
                "Message": "{\"AlarmName\":\"ContainerInsight-pod_cpu_utilization\",\"AlarmDescription\":null,\"AWSAccountId\":\"257706363616\",\"NewStateValue\":\"OK\",\"NewStateReason\":\"Thresholds Crossed: 1 out of the last 1 datapoints [0.46522264287069004 (27/06/21 13:52:00)] was not less than the lower thresholds [0.4129373661576242] or not greater than the upper thresholds [0.4700330400585261] (minimum 1 datapoint for ALARM -> OK transition).\",\"StateChangeTime\":\"2021-06-27T13:53:39.351+0000\",\"Region\":\"Asia Pacific (Seoul)\",\"AlarmArn\":\"arn:aws:cloudwatch:ap-northeast-2:257706363616:alarm:ContainerInsight-pod_cpu_utilization\",\"OldStateValue\":\"ALARM\",\"Trigger\":{\"Period\":60,\"EvaluationPeriods\":1,\"ComparisonOperator\":\"LessThanLowerOrGreaterThanUpperThreshold\",\"ThresholdMetricId\":\"ad1\",\"TreatMissingData\":\"- TreatMissingData:                    missing\",\"EvaluateLowSampleCountPercentile\":\"\",\"Metrics\":[{\"Id\":\"m1\",\"MetricStat\":{\"Metric\":{\"Dimensions\":[{\"value\":\"cloudone-dev-v1-eks-cluster\",\"name\":\"ClusterName\"}],\"MetricName\":\"pod_cpu_utilization\",\"Namespace\":\"ContainerInsights\"},\"Period\":60,\"Stat\":\"Average\"},\"ReturnData\":true},{\"Expression\":\"ANOMALY_DETECTION_BAND(m1, 0.592)\",\"Id\":\"ad1\",\"Label\":\"pod_cpu_utilization (expected)\",\"ReturnData\":true}]}}",
                "Signature": "LGJ46/jQIeVuIm8HngPVVholvGYSD2ul1C6erjiWH4PwcuDjYQOTLIdxbCzesH6KcqkUnHPKecF8yzdx4gxE70sT7rfyAEI+jcYNEkPLFJiRiwo3x3LquUu78Pud/pyjUMS7FiXajrxMw2D/t5KOf+o1//gejCZj+opuFNTe+lZ5Vr80mUKxwUtEz/KgXZ4tg9BMarTBJ3/1apg3Bs6gVRACiAz9Vy16vyrB1Nq9wsueV/Zin4zHJrlVHwAAVQhBhunfBW4+CySMZzeq1X8yyVqnlE4i29dW5fYxFzXdxrWbM8BjwCnK4au2UxwfvB6OJdgIpdiRbUn9Z0h9wnLcxw==",
                "MessageId": "448b4055-f4e5-5887-a547-190771c6686b",
                "UnsubscribeURL": "https://sns.ap-northeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-2:257706363616:spaceone-notification:4f9519e8-e213-4b33-b4a9-6cc24322f047",
                "Type": "Notification",
                "Timestamp": "2021-06-27T13:53:39.389Z"
            }
        }
        param1 = {
            "options": {},
            "data": {}
        }
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param.get('data')})
        print_json(parsed_data)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
