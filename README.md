# plugin-aws-sns-monitoring-webhook

![sns](https://user-images.githubusercontent.com/83386688/155678636-4e35b1d3-3fb6-4d1d-84aa-323a7f73b966.png)


**Webhook plugin for AWS SNS**

> SpaceONE's [plugin-aws-sns-monitoring-webhook](https://github.com/spaceone-dev/plugin-aws-sns-mon-webhook) 
 is a tool that can integrate and manage events of various patterns from various AWS alert services.   
> SpaceONE already supports various external monitoring ecosystems in the form of plug-ins   
> (Prometheus, Grafana, Zabbix, etc), and SNS webhook is one of them, which more reliably supports events of AWS alert services.

Find us also at [Dockerhub](https://hub.docker.com/repository/docker/spaceone/plugin-aws-sns-mon-webhook)
> Latest stable version : 1.1

Please contact us if you need any further information. (support@spaceone.dev)

---

## Supported Alert Services

Currently, you can receive the following events using AWS SNS webhook.
* AWS Cloudwatch
* AWS Health

If you need detailed AWS SNS settings to use the sns webhook.   
Please refer to the [SpaceONE Documentations](https://spaceone.org/docs/guides/alert_manager/webhook_settings/aws_sns_webhook/).

---

## Release note

### Ver 1.1

---

Refactoring   
- Add remove_code_in_title method
- Update get_namespace
- Modify severity_flag

### Ver 1.0

---

Update for cloud_metrics for aws cloudwatch type
