from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LedSwitchRequest(_message.Message):
    __slots__ = ["LedState"]
    LEDSTATE_FIELD_NUMBER: _ClassVar[int]
    LedState: bool
    def __init__(self, LedState: bool = ...) -> None: ...

class LedSwitchReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
