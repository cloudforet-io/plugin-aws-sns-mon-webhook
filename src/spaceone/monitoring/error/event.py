from spaceone.core.error import *


class ERROR_NOT_TITLE(ERROR_INVALID_ARGUMENT):
    _message = 'Title for Event message from AWS SNS is Missing (event = {event})'


class ERROR_PARSE_EVENT(ERROR_BASE):
    _message = 'Failed to parse event (field)'


class ERROR_GET_JSON_MESSAGE(ERROR_BASE):
    _message = 'Failed to get json (raw_json)'


class ERROR_NOT_DECISION_MANAGER(ERROR_BASE):
    _message = 'The received data type is a data type that is not currently supported.'
