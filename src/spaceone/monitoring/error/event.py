from spaceone.core.error import *

class ERROR_NOT_TITLE(ERROR_INVALID_ARGUMENT):
    _message = 'Title for Event message from AWS SNS is Missing (event = {event})'