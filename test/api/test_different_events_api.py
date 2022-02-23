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
        param1 = {"options": {},
                  "data": {
                      "SigningCertURL": "https://sns.ap-southeast-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                      "TopicArn": "arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev",
                      "Timestamp": "2022-02-18T08:35:33.452Z",
                      "Type": "Notification", "SignatureVersion": "1",
                      "Signature": "D1dd2IK8X+QUAZahFKkv0Ka8MKK7T3hPs9GKD6ANikv9UDV+cPGINMcfBB6EzL76aK4HnhL8vUTz/8bV46Xhh0EIVp0uepssk9ef7lh3dl69c3G63WtJM8WmLuWiQqvAILctKy9WLUl5twPQJJ+4n0wBFafWIvKGvwoA29E+QrwTsSOBk/7ZyfHRdeBBK/jNjwOBT1iJL9SIsT6+iOANr7SzhJ0Sk/SqjoQSZsb1TJvLXKu6I6D9Vv1yI/yfXdvtr4Ff6guBL6I+DE+6luQfxigzsUdsCjUlAbiLNmvsG44k6uMKfU22CwocBbLsuQkuYt73Kks4CaVE/vl+GsHc2g==",
                      "MessageId": "3737b6d6-1c86-59a2-9111-ec5f4013dd65",
                      "Message": "{\n  \"version\": \"0\",\n  \"id\": \"7bf73129-1428-4cd3-a780-95db273d1602\",\n  \"detail-type\": \"AWS Health Abuse Event\",\n  \"source\": \"aws.health\",\n  \"account\": \"123456789012\",\n  \"time\": \"2018-08-02T05:30:00Z\",\n  \"region\": \"global\",\n  \"resources\": [\"arn:aws:cloudfront::123456789012:distribution/DSF867DUMMY87SDF\", \"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd2222\"],\n  \"detail\": {\n    \"eventArn\": \"arn:aws:health:global::event/AWS_ABUSE_COPYRIGHT_DMCA_REPORT_2345235545_5323_2018_08_02_02_12_98\",\n    \"service\": \"ABUSE\",\n    \"eventTypeCode\": \"AWS_ABUSE_COPYRIGHT_DMCA_REPORT\",\n    \"eventTypeCategory\": \"issue\",\n    \"startTime\": \"Thu, 02 Aug 2018 05:30:00 GMT\",\n    \"eventDescription\": [{\n      \"language\": \"en_US\",\n      \"latestDescription\": \"A description of the event will be provided here\"\n    }],\n    \"affectedEntities\": [{\n      \"entityValue\": \"arn:aws:cloudfront::123456789012:distribution/DSF867DUMMY87SDF\"\n    }, {\n      \"entityValue\": \"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd2222\"\n    }]\n  }\n}",
                      "UnsubscribeURL": "https://sns.ap-southeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev:46b11fb0-b7d8-4ae9-934c-2593a89a79fb"}
                  }
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param.get('data')})
        print_json(parsed_data)
        print()
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param1.get('data')})
        print_json(parsed_data)
        print()


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)