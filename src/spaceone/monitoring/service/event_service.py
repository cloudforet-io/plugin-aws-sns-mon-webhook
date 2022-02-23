import logging
import json
from spaceone.core.service import *

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
        execute_manager = self._decision_manager(raw_data)
        _manager = self.locator.get_manager(execute_manager)
        parsed_event = _manager.parse(options, raw_data)
        _LOGGER.debug(f'[EventService: parse] {parsed_event}')
        return parsed_event

    @staticmethod
    def _decision_manager(raw_data):
        execute_manager = ''
        message = json.loads(raw_data.get("Message"))

        try:
            # cloudwatch manager
            if "AlarmArn" in message.keys():
                _, __, service, *___ = message.get("AlarmArn").split(":")
                if service == "cloudwatch":
                    execute_manager = "EventManager"
            # PHD manager
            if "source" in message.keys():
                _, service, *__ = message.get("source").split(".")
                if service == 'health':
                    execute_manager = "PersonalHealthDashboardManager"
        except Exception as e:
            _LOGGER.info(f'An unknown data has occurred {e}')
        return execute_manager
