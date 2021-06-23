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
        params = {
            "options": {

            },
            "data": {
                "MessageId": "e7c82e01-7cd8-5569-9ac1-774d893afc01",
                "Signature": "icuQY4hHf1yjCDy+XiWY0f1XvM3vv3X2wjfCcud1dnP/WHghBSOcpJmIonZRvsTNa6Y2ZL4+j95SnY0XiSlrtwQ5692ap3Ajez0WhVmcS7jUAvgCk3NfQV/H4zn7KryHoIvXB9fyjAnTZR4MnZ0AO5wV86XgD2ckBP8Gtl59HK7+B6BO/rsFxfS/x9MF3Qog3mDgR4fpvCYMhwYej4vRv38NLNYn9XVJnUPILHaTOfNG1NlJqBPslwXlV4ef5n86aPLJ8/nDsD1aSAVcOGfX9j/Z6aEF2FmM6hFz1+3ZfYOsu1dB8zGnVdHhNi7jNgqLmoY89WG3ZMDlUJTPDoui5A==",
                "TopicArn": "arn:aws:sns:ap-northeast-2:257706363616:spaceone-notification",
                "Message": "{\"AlarmName\":\"EC2-CPU\",\"AlarmDescription\":null,\"AWSAccountId\":\"257706363616\",\"NewStateValue\":\"ALARM\",\"NewStateReason\":\"Threshold Crossed: 1 out of the last 1 datapoints [17.2564528039004 (23/06/21 08:31:00)] was greater than the threshold (15.0) (minimum 1 datapoint for OK -> ALARM transition).\",\"StateChangeTime\":\"2021-06-23T08:41:06.622+0000\",\"Region\":\"Asia Pacific (Seoul)\",\"AlarmArn\":\"arn:aws:cloudwatch:ap-northeast-2:257706363616:alarm:EC2-CPU\",\"OldStateValue\":\"INSUFFICIENT_DATA\",\"Trigger\":{\"MetricName\":\"CPUUtilization\",\"Namespace\":\"AWS/EC2\",\"StatisticType\":\"Statistic\",\"Statistic\":\"AVERAGE\",\"Unit\":null,\"Dimensions\":[{\"value\":\"i-0f672ea50a80cda4b\",\"name\":\"InstanceId\"}],\"Period\":300,\"EvaluationPeriods\":1,\"ComparisonOperator\":\"GreaterThanThreshold\",\"Threshold\":15.0,\"TreatMissingData\":\"- TreatMissingData: missing\",\"EvaluateLowSampleCountPercentile\":\"\"}}",
                "Type": "Notification",
                "UnsubscribeURL": "https://sns.ap-northeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-2:257706363616:spaceone-notification:4f9519e8-e213-4b33-b4a9-6cc24322f047",
                "Timestamp": "2021-06-23T08:41:06.656Z",
                "SigningCertURL": "https://sns.ap-northeast-2.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",
                "Subject": "ALARM: \"EC2-CPU\" in Asia Pacific (Seoul)",
                "SignatureVersion": "1"
            }
        }
        param1 = {
            "options": {},
            "data": {}
        }
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param1.get('data')})
        print_json(parsed_data)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
