import logging
import requests
import json
from spaceone.core.service import *

from spaceone.monitoring.error.event import ERROR_PARSE_EVENT

_LOGGER = logging.getLogger(__name__)


@authentication_handler
@authorization_handler
@event_handler
class EventService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @transaction
    @check_required(['options', 'data'])
    def parse(self, params):
        """

        Args:
            params (dict): {
                'options': 'dict',
                'raw_data': 'dict'
            }

        Returns:
            plugin_metric_data_response (dict)

        """

        options = params.get('options')
        raw_data = params.get('data')

        try:
            if raw_data.get('Type') == 'SubscriptionConfirmation':
                self._request_subscription_confirm(raw_data.get('SubscribeURL'))
                return []
            else:
                execute_manager = self._decision_manager(raw_data)
                _manager = self.locator.get_manager(execute_manager)
                parsed_event = _manager.parse(options, raw_data)
                _LOGGER.debug(f'[EventService: parse] {parsed_event}')
                return parsed_event
        except Exception as e:
            raise ERROR_PARSE_EVENT(field=e)

    @staticmethod
    def _request_subscription_confirm(confirm_url):
        r = requests.get(confirm_url)
        _LOGGER.debug(f'[Confirm_URL: SubscribeURL] {confirm_url}')
        _LOGGER.debug(f'[AWS SNS: Status]: {r.status_code}, {r.content}')

    @staticmethod
    def _decision_manager(raw_data):
        execute_manager = ''
        message = json.loads(raw_data.get("Message", "{}"))

        # cloudwatch manager
        if "AlarmArn" in message.keys():
            service = message.get("AlarmArn").split(":")[2]
            if service == "cloudwatch":
                execute_manager = "EventManager"
            return execute_manager

        # PHD manager
        elif "source" in message.keys():
            service = message.get("source").split(".")[1]
            if service == 'health':
                execute_manager = "PersonalHealthDashboardManager"
            return execute_manager
        else:
            raise Exception(f'An unknown data has occurred')
