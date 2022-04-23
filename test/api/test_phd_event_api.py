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
        param = {"options": {},
                 "data": {
                     "MessageId": "3f78eee9-6691-51be-b77e-b4603c34d486", "Timestamp": "2022-02-18T08:27:17.407Z",
                     "TopicArn": "arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev", "SignatureVersion": "1",
                     "Type": "Notification",
                     "SigningCertURL": "https://sns.ap-southeast-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                     "UnsubscribeURL": "https://sns.ap-southeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev:46b11fb0-b7d8-4ae9-934c-2593a89a79fb",
                     "Message": "{\n  \"version\": \"0\",\n  \"id\": \"7bf73129-1428-4cd3-a780-95db273d1602\",\n  \"detail-type\": \"AWS Health Event\",\n  \"source\": \"aws.health\",\n  \"account\": \"123456789012\",\n  \"time\": \"2016-06-05T06:27:57Z\",\n  \"region\": \"ap-southeast-2\",\n  \"resources\": [],\n  \"detail\": {\n    \"eventArn\": \"arn:aws:health:ap-southeast-2::event/AWS_ELASTICLOADBALANCING_API_ISSUE_90353408594353980\",\n    \"service\": \"ELASTICLOADBALANCING\",\n    \"eventTypeCode\": \"AWS_ELASTICLOADBALANCING_API_ISSUE\",\n    \"eventTypeCategory\": \"issue\",\n    \"startTime\": \"Sat, 04 Jun 2016 05:01:10 GMT\",\n    \"endTime\": \"Sat, 04 Jun 2016 05:30:57 GMT\",\n    \"eventDescription\": [{\n      \"language\": \"en_US\",\n      \"latestDescription\": \"A description of the event will be provided here\"\n    }]\n  }\n}",
                     "Signature": "X/CKfxDEiAOUmx9exJHB0ChOMwxOy+pzvb37OP3NA9c1ttVy5CDRkHa8lTLnos3h7CYSzdKFaUMWp/xhIbdXeRzM/HzaVUH+GseJrZFZDi1dvMSjtbacmSNO2Sxkjc6yaqht9zyh3C/8BEN1uQuCQh5bGriV2Ty4/LrxvrX/y4qF2JWmXnQacsaOWYqQWUBLcoPS19fD5X+Cs9OunQW1ZdWGPVumTC8gx3Pdx1Zf7Htd7sz5JXmiryMVCyP8iBWAdpjycVIZJV2+OcjQ5Vv+L52zkiU9Y3EUYgCmx8mkOR6SGjfasL0KfQ890mMR7+MsOqRgMFKakesFq9COzgp55Q=="}
                 }
        param1 = {"options": {},
                  "data": {
                      "Signature": "O965M1pBN5oCvh5DRyvoYjV8eaZjUwS/o0CR7/ddCwYfpDXkprAELHyDHp5KDy1Hs+6ZP19BWXPhejPzgJKkkfz6R4/oVyDEVF+NTKLNl9Khq2EDSlpP6LhYMpu5rjyOMseu5OB/5YJN0EFlo/a8I1QBZBaRcpG3swfDTRg2/hLRy92JIFkO0WHlK0iVCMntMnsEg5WDQ+kzXqUIqKIihI81y+0sS15eiXiUJ38IDdPeEVDeQrvuZHfc2yAxqRC0L1c206ZqOOdf8gkW3MXcoFfwiPgZQgFQxwJ/9z065ZGvSSlmuQ/R17z2VmQTouL6b7l7LjaZ9fPFksIdAca5sw==",
                      "SignatureVersion": "1",
                      "Message": "{\n  \"version\": \"0\",\n  \"id\": \"7bf73129-1428-4cd3-a780-95db273d1602\",\n  \"detail-type\": \"AWS Health Event\",\n  \"source\": \"aws.health\",\n  \"account\": \"123456789012\",\n  \"time\": \"2016-06-05T06:27:57Z\",\n  \"region\": \"us-west-2\",\n  \"resources\": [\"i-abcd1111\"],\n  \"detail\": {\n    \"eventArn\": \"arn:aws:health:us-west-2::event/AWS_EC2_INSTANCE_STORE_DRIVE_PERFORMANCE_DEGRADED_90353408594353980\",\n    \"service\": \"EC2\",\n    \"eventTypeCode\": \"AWS_EC2_INSTANCE_STORE_DRIVE_PERFORMANCE_DEGRADED\",\n    \"eventTypeCategory\": \"issue\",\n    \"startTime\": \"Sat, 05 Jun 2016 15:10:09 GMT\",\n    \"eventDescription\": [{\n      \"language\": \"en_US\",\n      \"latestDescription\": \"A description of the event will be provided here\"\n    }],\n    \"affectedEntities\": [{\n      \"entityValue\": \"i-abcd1111\",\n      \"tags\": {\n        \"stage\": \"prod\",\n        \"app\": \"my-app\"\n      }\n    }]\n  }\n}",
                      "SigningCertURL": "https://sns.ap-southeast-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                      "Timestamp": "2022-02-18T08:32:39.194Z", "Type": "Notification",
                      "UnsubscribeURL": "https://sns.ap-southeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev:46b11fb0-b7d8-4ae9-934c-2593a89a79fb",
                      "TopicArn": "arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev",
                      "MessageId": "8c9bce44-3a81-544d-bd36-94cd6166fb31"}
                  }
        param2 = {"options": {},
                  "data": {
                      "UnsubscribeURL": "https://sns.ap-southeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev:46b11fb0-b7d8-4ae9-934c-2593a89a79fb",
                      "MessageId": "5f348269-339e-5e41-88e6-d8e06fc1989f", "SignatureVersion": "1",
                      "Type": "Notification",
                      "Signature": "oar3KkfeJFzrmFmchcYjH6Sqx0TjgUs/YZ/9FIR8YopYMqCDSX8eZQYmfJQXR8gkuc8ZnCvqAEJ72XFHkIZERTrr2sDeZJ/e85ukZoIaAIsLkuEM4QvyZJOcLTTmqoFC1/NWj/QdJTExBvx9E0Opr+YA4BV5TTUdqXo4JJY5aYYlE25JQmmOCRUAVeTYFkTAmBE0kd03flRkpPR4Gib21pnlTYD4bfAttr2k+hPq8r8w1s8wJnu5u0ua6qKdyTvfQMX6Fx/eSk8OgPDTFZRslvMDQixGS/aLF1D5im7nwMlRkPQn4jAKGyXPLrs5KB5Mn89NGUwDCPt41LENfvFoiQ==",
                      "Message": "{\n  \"version\": \"0\",\n  \"id\": \"7bf73129-1428-4cd3-a780-95db273d1602\",\n  \"detail-type\": \"AWS Health Abuse Event\",\n  \"source\": \"aws.health\",\n  \"account\": \"123456789012\",\n  \"time\": \"2018-08-01T06:27:57Z\",\n  \"region\": \"global\",\n  \"resources\": [\"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111\", \"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd2222\"],\n  \"detail\": {\n    \"eventArn\": \"arn:aws:health:global::event/AWS_ABUSE_DOS_REPORT_92387492375_4498_2018_08_01_02_33_00\",\n    \"service\": \"ABUSE\",\n    \"eventTypeCode\": \"AWS_ABUSE_DOS_REPORT\",\n    \"eventTypeCategory\": \"issue\",\n    \"startTime\": \"Wed, 01 Aug 2018 06:27:57 GMT\",\n    \"eventDescription\": [{\n      \"language\": \"en_US\",\n      \"latestDescription\": \"A description of the event will be provided here\"\n    }],\n    \"affectedEntities\": [{\n      \"entityValue\": \"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111\"\n    }, {\n      \"entityValue\": \"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd2222\"\n    }]\n  }\n}",
                      "SigningCertURL": "https://sns.ap-southeast-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                      "Timestamp": "2022-02-18T08:34:39.768Z",
                      "TopicArn": "arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev"}
                  }
        param3 = {"options": {},
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

        param4 = {"options": {},
                  "data": {
                      "MessageId": "4be4288a-ce0d-5066-9059-724de0d178ee",
                      "UnsubscribeURL": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:1234567890:spaceone-dev-sns-webhook-for-health-disabled:ad959fca-f054-4cca-98f0-36e4db62xxxx",
                      "Timestamp": "2022-04-06T06:01:00.180Z",
                      "SignatureVersion": "1",
                      "Message": "{\"version\":\"0\",\"id\":\"2345b410-2a1b-cc03-468a-92610013xxxx\",\"detail-type\":\"AWS Health Event\",\"source\":\"aws.health\",\"account\":\"1234567890\",\"time\":\"2022-04-06T06:00:53Z\",\"region\":\"us-east-1\",\"resources\":[\"arn:aws:acm:us-east-1:1234567890:certificate/95d1b7f1-5e04-4c70-9a95-73764d4xxxxx\"],\"detail\":{\"eventArn\":\"arn:aws:health:us-east-1::event/ACM/AWS_ACM_RENEWAL_STATE_CHANGE/AWS_ACM_RENEWAL_STATE_CHANGE-837a9d58-dd89-441a-bee9-fea9425565e2\",\"service\":\"ACM\",\"eventTypeCode\":\"AWS_ACM_RENEWAL_STATE_CHANGE\",\"eventTypeCategory\":\"scheduledChange\",\"startTime\":\"Wed, 6 Apr 2022 06:00:53 GMT\",\"endTime\":\"Wed, 6 Apr 2022 06:00:53 GMT\",\"eventDescription\":[{\"language\":\"en_US\",\"latestDescription\":\"This is to notify you that AWS Certificate Manager (ACM) has completed the renewal of an SSL/TLS certificate that certificate includes the primary domain storybook.developer.spaceone.dev and a total of 1 domains.\\\\\\\\n\\\\\\\\nAWS account ID: 1234567890\\\\\\\\nAWS Region name: us-east-1\\\\\\\\nCertificate identifier: arn:aws:acm:us-east-1:1234567890:certificate/95d1b7f1-5e04-4c70-9a95-73764d4xxxxx\\\\\\\\n\\\\\\\\nYour new certificate expires on May 05, 2023 at 23:59:59 UTC. \\\\\\\\nIf you have questions about this process, please use the Support Center at https://console.aws.amazon.com/support to contact AWS Support. If you don’t have an AWS support plan, post a new thread in the AWS Certificate Manager discussion forum at https://forums.aws.amazon.com/forum.jspa?forumID=206\\\\\\\\n\\\\\\\\nThis notification is intended solely for authorized individuals for storybook.developer.spaceone.dev. To express any concerns about this notification or if it has reached you in error, forward it along with a brief explanation of your concern to validation-questions@amazon.com.\\\\\\\\n\"}],\"affectedEntities\":[{\"entityValue\":\"arn:aws:acm:us-east-1:1234567890:certificate/95d1b7f1-5e04-4c70-9a95-73764d4dxxxx\"}]}}",
                      "Signature": "CDes02KXXXX+C3c43UgAf51M4VCdZtNclXe98vbp74og8shNZoXg2s6RbyrXwmAxznCDfkDJUZnl2QP8vO/Z1atD0RZHfZVUNVZaaCErOHD79QDrQn8VGj75JUEg3XrhFlI7qDJBFm6L+8Qr87CTI5YEZ2NXzXXXXX/7ULHp+DISGQxRyNEYyR9+Fuyi2QXnjqQPm3SXsKFeoZ9nQyRuIAJ0xzGA8ywhKPUk6Vb8DXSJbJwJv+WOKIpQGfK61MTWw5/CmvP9OVYid01PCM/vof/L47xytSgJd4WIzCMoG9mLKD8YahwrjH3NF72nVUjxd6kPXXXXX/NcWIZCosaxeA==",
                      "TopicArn": "arn:aws:sns:us-east-1:1234567890:spaceone-dev-sns-webhook-for-health-disabled",
                      "SigningCertURL": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                      "Type": "Notification"}
                  }

        # None-primitive type
        param5 = {
            "options": {},
            "data": {
                "detail-type": "AWS Health Event",
                "region": "us-east-1",
                "detail": {
                    "startTime": "Wed, 6 Apr 2022 06:00:53 GMT",
                    "eventArn": "arn:aws:health:us-east-1::event/ACM/AWS_ACM_RENEWAL_STATE_CHANGE/AWS_ACM_RENEWAL_STATE_CHANGE-837a9d58-dd89-441a-bee9-fea9425565e2",
                    "endTime": "Wed, 6 Apr 2022 06:00:53 GMT",
                    "affectedEntities": [{
                        "entityValue": "arn:aws:acm:us-east-1:257706363616:certificate/95d1b7f1-5e04-4c70-9a95-73764d4d0fc5"}],
                    "service": "ACM",
                    "eventDescription": [{
                        "latestDescription": "This is to notify you that AWS Certificate Manager (ACM) has completed the renewal of an SSL/TLS certificate that certificate includes the primary domain storybook.developer.spaceone.dev and a total of 1 domains.\\\\n\\\\nAWS account ID: 257706363616\\\\nAWS Region name: us-east-1\\\\nCertificate identifier: arn:aws:acm:us-east-1:257706363616:certificate/95d1b7f1-5e04-4c70-9a95-73764d4d0fc5\\\\n\\\\nYour new certificate expires on May 05, 2023 at 23:59:59 UTC. \\\\nIf you have questions about this process, please use the Support Center at https://console.aws.amazon.com/support to contact AWS Support. If you don\u2019t have an AWS support plan, post a new thread in the AWS Certificate Manager discussion forum at https://forums.aws.amazon.com/forum.jspa?forumID=206\\\\n\\\\nThis notification is intended solely for authorized individuals for storybook.developer.spaceone.dev. To express any concerns about this notification or if it has reached you in error, forward it along with a brief explanation of your concern to validation-questions@amazon.com.\\\\n",
                        "language": "en_US"
                    }],
                    "eventTypeCategory": "scheduledChange",
                    "eventTypeCode": "AWS_ACM_RENEWAL_STATE_CHANGE"
                },
                "time": "2022-04-06T06:00:53Z",
                "source": "aws.health",
                "version": "0",
                "id": "2345b410-2a1b-cc03-468a-92610013fea5",
                "resources": [
                    "arn:aws:acm:us-east-1:257706363616:certificate/95d1b7f1-5e04-4c70-9a95-73764d4d0fc5"
                ],
                "account": "257706363616"
            }
        }
        param6 = {
            "options": {},
            "data": {
                "detail": {
                    "affectedEntities": [
                        {
                            "entityValue": "arn:aws:iam::257706363616:user/jihyung.song"
                        }
                    ],
                    "startTime": "Thu, 21 Apr 2022 00:00:00 GMT",
                    "eventTypeCode": "AWS_CLOUDSHELL_PERSISTENCE_EXPIRING",
                    "eventArn": "arn:aws:health:us-east-1::event/CLOUDSHELL/AWS_CLOUDSHELL_PERSISTENCE_EXPIRING/AWS_CLOUDSHELL_PERSISTENCE_EXPIRING_v20220208_257706363616_us-east-1_23-4-2022",
                    "service": "CLOUDSHELL",
                    "eventDescription": [
                        {
                            "latestDescription": "Some users of this account haven't used AWS CloudShell for over 110 days in the us-east-1 Region. On April 23, 2022 we're scheduled to delete the CloudShell home directory and data of inactive users in the us-east-1 Region.\\n\\nYou can see the list of affected users in the Affected Resources tab. To stop this deletion, users that are listed in the Affected Resources tab need to launch CloudShell https://us-east-1.console.aws.amazon.com/cloudshell/home?region=us-east-1# in the us-east-1 Region.\\n\\nImportant: AWS CloudShell offers a separate home directory per AWS Region, so the deletion of the home directory will occur only in the AWS Region that hasn't been used for your CloudShell sessions in over 120 days. If you regularly use CloudShell in other AWS Regions, those separate home directories will not be affected.\\n\\nVisit https://docs.aws.amazon.com/cloudshell/latest/userguide/limits.html#persistent-storage-limitations if you'd like more information on persistent storage in AWS CloudShell.",
                            "language": "en_US"
                        }
                    ],
                    "endTime": "Sat, 23 Apr 2022 21:46:18 GMT",
                    "eventTypeCategory": "scheduledChange"
                },
                "region": "us-east-1",
                "id": "3369231b-01e5-5063-33d4-941d984ec455",
                "detail-type": "AWS Health Event",
                "resources": [
                    "arn:aws:iam::257706363616:user/jihyung.song"
                ],
                "version": "0",
                "account": "257706363616",
                "time": "2022-04-21T00:00:00Z",
                "source": "aws.health"
            }
        }

        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param.get('data')})
        print_json(parsed_data)
        print()
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param1.get('data')})
        print_json(parsed_data)
        print()
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param2.get('data')})
        print_json(parsed_data)
        print()
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param3.get('data')})
        print_json(parsed_data)
        print()
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param4.get('data')})
        print_json(parsed_data)
        print()
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param5.get('data')})
        print_json(parsed_data)
        print()
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param6.get('data')})
        print_json(parsed_data)
        print()


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
