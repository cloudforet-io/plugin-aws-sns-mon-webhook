## 소개

**AWS SNS**(Simple Notification Service)는 마이크로서비스 및 서버리스 애플리케이션을 위한 Pub/Sub 메시징 서비스입니다. 

클라우드포레는 **AWS SNS webhook 플러그인**을 사용하여 AWS SNS 구독을 통해 전달되는 이벤트를 수신합니다.

현재까지 클라우드 포레에서 AWS SNS webhook으로 수집할 수 있는 이벤트는  
**PHD(PersonalHealthDashboard)** 이벤트와 **CloudWatch** 이벤트로 나눌 수 있습니다.

PHD 이벤트는 AWS Health에서 발생하는 데이터를 의미하고  
CloudWatch 이벤트는 AWS CloudWatch에서 발생하는 이벤트로 애플리케이션과 인프라 리소스을 모니터링 중 발생하는 이벤트를 의미합니다.

AWS SNS Webhook으로 수집할 수 있는 서비스에 대한 자세한 목록은 [Supported Alert Services](https://github.com/spaceone-dev/plugin-aws-sns-mon-webhook#supported-alert-services) 에서 확인할 수 있습니다.  
추후 또 다른 AWS 서비스 개발이 완료되면 위의 목록에서 확인 가능합니다.

설정에 관한 상세 가이드는 아래 링크를 통해 확인할 수 있습니다.

1. [AWS PersonalHealthDashboard 설정](./PersonalHealthDashboard.md)
2. [AWS CloudWatch 설정](./CloudWatch.md)