import logging
import unittest
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json
from pprint import pprint

_LOGGER = logging.getLogger(__name__)


class TestEvent(TestCase):
    def test_parse(self):
        params = {"options": {}, "data": {"Type": "Notification", "Message": "{\"AlarmName\":\"ec2CPUUtilization\",\"AlarmDescription\":\"EC2 CPUUtilization sample\",\"AWSAccountId\":\"257706363616\",\"NewStateValue\":\"OK\",\"NewStateReason\":\"Threshold Crossed: 1 out of the last 1 datapoints [5.477211732525876 (18/06/21 04:23:00)] was not greater than the threshold (5.5) (minimum 1 datapoint for ALARM -> OK transition).\",\"StateChangeTime\":\"2021-06-18T04:28:21.914+0000\",\"Region\":\"Asia Pacific (Tokyo)\",\"AlarmArn\":\"arn:aws:cloudwatch:ap-northeast-1:257706363616:alarm:ec2CPUUtilization\",\"OldStateValue\":\"ALARM\",\"Trigger\":{\"MetricName\":\"CPUUtilization\",\"Namespace\":\"AWS/EC2\",\"StatisticType\":\"Statistic\",\"Statistic\":\"AVERAGE\",\"Unit\":null,\"Dimensions\":[{\"value\":\"eks-6ebcce7e-400b-8a69-f0e9-d9e14bb635d2\",\"name\":\"AutoScalingGroupName\"}],\"Period\":300,\"EvaluationPeriods\":1,\"ComparisonOperator\":\"GreaterThanThreshold\",\"Threshold\":5.5,\"TreatMissingData\":\"- TreatMissingData: missing\",\"EvaluateLowSampleCountPercentile\":\"\"}}", "UnsubscribeURL": "https://sns.ap-northeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-1:257706363616:aws-sns-topic:1d86153d-18f4-4099-8352-eaba66db445e", "Signature": "d19DSamZjhSX3Got6fzh/a20o3TqwY2Mu95Zd7f8xzDfp6QhDVR7r7Tyf9NjtvYt5jJaJZmeyIkAMUAnXEHKvJCZhMnQJO+/H4YtOuW+jRNyFJFhfoHY5M6nIhkfl69BANOxM2AwGk6tsHHJiTRvN9zJdWZpI3H26nbWLn/0s0ffbemfQrNCnyE17BsURoeYfG302hl5Np3tSS4kd35YspeRQ1s5CYYsGKE8cIlRbh/V8SNQvmotoM/b1quIbBbsj6yCz5D4WTcUdyoxY0bbu/dN9PvXYGenAstPZOcENfR+sK+s7bnc9HdyZbGuD7OsqfZdj913045ivXXbFS3++Q==", "TopicArn": "arn:aws:sns:ap-northeast-1:257706363616:aws-sns-topic", "SigningCertURL": "https://sns.ap-northeast-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem", "Timestamp": "2021-06-18T04:28:21.967Z", "Subject": "OK: \"ec2CPUUtilization\" in Asia Pacific (Tokyo)", "SignatureVersion": "1", "MessageId": "d22096fc-c983-57a6-805d-cfbaeaa69dde"}}
        options = params.get("options")
        data = params.get("data")

        parsed_data = self.monitoring.Event.parse({'options': options, 'data': data})
        print_json(parsed_data)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
