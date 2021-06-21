import logging
import unittest
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json
from pprint import pprint

_LOGGER = logging.getLogger(__name__)


class TestEvent(TestCase):
    def test_parse(self):
        params = {"options": {}, "data": {"Type": "Notification", "UnsubscribeURL": "https://sns.ap-northeast-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-1:257706363616:aws-sns-topic:1d86153d-18f4-4099-8352-eaba66db445e", "SignatureVersion": "1", "MessageId": "20a65051-dd7d-5952-906e-09179028dc41", "TopicArn": "arn:aws:sns:ap-northeast-1:257706363616:aws-sns-topic", "Timestamp": "2021-06-18T07:28:21.978Z", "Message": "{\"AlarmName\":\"ec2CPUUtilization\",\"AlarmDescription\":\"EC2 CPUUtilization sample\",\"AWSAccountId\":\"257706363616\",\"NewStateValue\":\"OK\",\"NewStateReason\":\"Threshold Crossed: 1 out of the last 1 datapoints [5.470572292836039 (18/06/21 07:23:00)] was not greater than the threshold (5.5) (minimum 1 datapoint for ALARM -> OK transition).\",\"StateChangeTime\":\"2021-06-18T07:28:21.921+0000\",\"Region\":\"Asia Pacific (Tokyo)\",\"AlarmArn\":\"arn:aws:cloudwatch:ap-northeast-1:257706363616:alarm:ec2CPUUtilization\",\"OldStateValue\":\"ALARM\",\"Trigger\":{\"MetricName\":\"CPUUtilization\",\"Namespace\":\"AWS/EC2\",\"StatisticType\":\"Statistic\",\"Statistic\":\"AVERAGE\",\"Unit\":null,\"Dimensions\":[{\"value\":\"eks-6ebcce7e-400b-8a69-f0e9-d9e14bb635d2\",\"name\":\"AutoScalingGroupName\"}],\"Period\":300,\"EvaluationPeriods\":1,\"ComparisonOperator\":\"GreaterThanThreshold\",\"Threshold\":5.5,\"TreatMissingData\":\"- TreatMissingData: missing\",\"EvaluateLowSampleCountPercentile\":\"\"}}", "Subject": "OK: \"ec2CPUUtilization\" in Asia Pacific (Tokyo)", "SigningCertURL": "https://sns.ap-northeast-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem", "Signature": "CTxotu3AhSgNZoaqDWZCm7hAPHTSwn5gby35fHV0MJS/aMTKOFymUhFlPU1eOoCFJUFksFDrIWv3cD88wbxFl6Hyi6Klo5tQ4I+W0GMzNFfFNTXdwq0wHSxdKk6nP9DpRxQwxqXBrJQXVNiN2PM61OmMRphFzA0vUKFGQKfM7V148+DgHrDJQkaqtuvnXe9YSjaI3l7GuQCeK2bDEtPMOxgY0h3D92GT/ykLHnPNfiG3z+8OsRWKs3F92kNVMNHbUMiCI6Eg+prv81ACyTf7AHvI9jwcuDNGMGdoQ/xKhsbN21EmBeHMeE8YG0U67Cp8icLQiHrNkJj2UEsqYnPH+w=="}}
        options = params.get("options")
        data = params.get("data")

        parsed_data = self.monitoring.Event.parse({'options': options, 'data': data})
        print_json(parsed_data)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
