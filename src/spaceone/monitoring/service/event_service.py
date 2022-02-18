import logging
from spaceone.core.service import *
from spaceone.monitoring.manager.event_manager import EventManager

_LOGGER = logging.getLogger(__name__)


@authentication_handler
@authorization_handler
@event_handler
class EventService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #TODO: EventManager와 PersonalHealthDashboardManager 구별하는 다른 방안 마련해야 함
        self.event_mgr: EventManager = self.locator.get_manager('PersonalHealthDashboardManager')

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
        parsed_event = self.event_mgr.parse(options, raw_data)
        _LOGGER.debug(f'[EventService: parse] {parsed_event}')
        return parsed_event
