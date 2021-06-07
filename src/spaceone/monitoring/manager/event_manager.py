import logging
import requests
from spaceone.core.manager import BaseManager
from spaceone.monitoring.error import *
_LOGGER = logging.getLogger(__name__)


class EventManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse(self, options, raw_data):
        ### parsing raw_data ####
        default_parsed_data = []

        request = raw_data.get('request', {})
        header = request.get('header', {})

        if header.get('X-Amz-Sns-Message-Type') == 'SubscriptionConfirmation':
            subscribe_url = request.get('SubscribeURL')
            _LOGGER.debug(f'[Confirm_URL: SubscribeURL] {subscribe_url}')
            r = requests.get(subscribe_url)
            _LOGGER.debug(f'[AWS SNS: Status]: {r.status_code}, {r.content}')

        return default_parsed_data
