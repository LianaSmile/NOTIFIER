from typing import Optional, Union
from src.infrastructure.services import LoggerService


class EnvItemEntity:
    def __init__(self, key: str, value: str):
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value


class EventEntity:
    def __init__(self, event_type: str, body: Union[str, dict], to: Optional[str] = None):
        self._logger_service = None
        self._verify_event_type(event_type)
        self._body = body
        self._to = to

    def _verify_event_type(self, event_type):
        if event_type not in ["new_publication", "approved_publication"]:
            self._event_type = None
            self.logger_service.warning(f"Invalid Event Type - {event_type}")
        else:
            self._event_type = event_type

    @property
    def logger_service(self) -> LoggerService:
        if self._logger_service is None:
            self._logger_service = LoggerService(__name__).logger
        return self._logger_service

    @property
    def event_type(self):
        return self._event_type

    @property
    def body(self):
        return self._body

    @property
    def to(self):
        return self._to
