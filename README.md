<h1 align="center">AWS SNS Webhook Plugin</h1>  

<br/>  
<div align="center" style="display:flex;">  
  <img width="245" src="https://user-images.githubusercontent.com/83386688/155678636-4e35b1d3-3fb6-4d1d-84aa-323a7f73b966.png">
  <p> 
    <br>
    <img alt="Version"  src="https://img.shields.io/badge/version-1.2.1-blue.svg?cacheSeconds=2592000"  />    
    <a href="https://www.apache.org/licenses/LICENSE-2.0"  target="_blank"><img alt="License: Apache 2.0"  src="https://img.shields.io/badge/License-Apache 2.0-yellow.svg" /></a> 
  </p> 
</div>    

**Webhook plugin for AWS SNS**

> SpaceONE's [plugin-aws-sns-monitoring-webhook](https://github.com/spaceone-dev/plugin-aws-sns-mon-webhook) 
 is a tool that can integrate and manage events of various patterns from various AWS alert services.   
> SpaceONE already supports various external monitoring ecosystems in the form of plug-ins   
> (Prometheus, Grafana, Zabbix, etc), and SNS webhook is one of them, which more reliably supports events of AWS alert services.

Find us also at [Dockerhub](https://hub.docker.com/repository/docker/spaceone/plugin-aws-sns-mon-webhook)
> Latest stable version : 1.2.1

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


### Ver 1.2.2

---

Enhancement
- Apply regardless of primitive type about phd events ([#50](https://github.com/spaceone-dev/plugin-aws-sns-mon-webhook/issues/50))
- change to receive paragraph-delimited scription ([#48](https://github.com/spaceone-dev/plugin-aws-sns-mon-webhook/issues/48))

### Ver 1.2.1

---

Enhancement
- Add provider field and account field (#47)
- Add affected entities in discription (#46)

Test
- Add test code about Event Service (#46)




### Ver 1.2

---

Enhancement
- Apply PersonalHealthDashboard Event (#39, #41)

Refactoring
- Modify affectedEntities type (#44)
- Add account info in discription(#41)


### Ver 1.1

---

Refactoring   
- Add remove_code_in_title method (#37)
- Update get_namespace (#35)
- Modify severity_flag (#27)

### Ver 1.0

---

Enhancement
- Update for cloud_metrics for aws cloudwatch type (#29)
