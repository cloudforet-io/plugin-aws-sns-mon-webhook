import logging
import requests
import json
from spaceone.core.service import *

from spaceone.monitoring.error.event import ERROR_PARSE_EVENT, ERROR_NOT_DECISION_MANAGER

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
                message = self.get_message(raw_data)

                execute_manager = self._decision_manager(message)
                _manager = self.locator.get_manager(execute_manager)

                if execute_manager == 'EventManager':
                    message['subject'] = raw_data.get('Subject', '')

                parsed_event = _manager.parse(options, message)
                _LOGGER.debug(f'[EventService: parse] {parsed_event}')
                return parsed_event
        except Exception as e:
            raise ERROR_PARSE_EVENT(field=e)

    @staticmethod
    def _request_subscription_confirm(confirm_url):
        r = requests.get(confirm_url)
        _LOGGER.debug(f'[Confirm_URL: SubscribeURL] {confirm_url}')
        _LOGGER.debug(f'[AWS SNS: Status]: {r.status_code}, {r.content}')

    def _decision_manager(self, message):
        execute_manager = ''

        if "AlarmArn" in message:
            service = message.get("AlarmArn").split(":")[2]
            if service == "cloudwatch":
                execute_manager = "EventManager"
            return execute_manager
        elif message.get('source').split(".")[1] == 'health':
            execute_manager = "PersonalHealthDashboardManager"
            return execute_manager
        else:
            raise ERROR_NOT_DECISION_MANAGER()

    @staticmethod
    def get_message(raw_data):
        if 'Message' in raw_data:
            message = json.loads(raw_data.get("Message", "{}"))
        else:
            message = raw_data

        return message
