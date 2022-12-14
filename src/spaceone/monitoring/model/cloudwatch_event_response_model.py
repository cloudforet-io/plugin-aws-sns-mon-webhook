from schematics.models import Model
from schematics.types import StringType, ModelType, DateTimeType

__all__ = ['EventModel']


class CloudWatchAdditionalInfo(Model):
    AWSAccountId = StringType(required=True)
    AlarmArn = StringType(required=True)
    AlarmName = StringType()
    OldStateValue = StringType()
    Region = StringType()
    MetricName = StringType()
    Namespace = StringType()


class ResourceModel(Model):
    resource_id = StringType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)
    ip_address = StringType(serialize_when_none=False)
    resource_type = StringType(serialize_when_none=False)


class EventModel(Model):
    event_key = StringType(required=True)
    event_type = StringType(choices=['RECOVERY', 'ALERT'], default='ALERT')
    title = StringType(required=True)
    description = StringType(default='')
    severity = StringType(choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'NOT_AVAILABLE'], default=None)
    resource = ModelType(ResourceModel)
    rule = StringType(default='')
    occurred_at = DateTimeType()
    provider = StringType(default='aws')
    account = StringType(default='')
    additional_info = ModelType(CloudWatchAdditionalInfo)