__all__ = ['PluginInfo', 'EventsInfo']

from spaceone.api.monitoring.plugin import webhook_pb2, event_pb2
from spaceone.core.pygrpc.message_type import *


def PluginInfo(result):
    result['metadata'] = change_struct_type(result['metadata'])
    return webhook_pb2.PluginInfo(**result)


def EventsInfo(event_info_dict):
    print(event_info_dict)
    event_info_dict['results'] = change_struct_type(event_info_dict['results'])
    return event_pb2.EventsInfo(**event_info_dict)