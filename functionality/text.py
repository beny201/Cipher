from dataclasses import dataclass
from typing import Optional


@dataclass
class Text:
    _message: str = "Empty"
    _rot_type: Optional[str] = None
    _status: str = "decrypted"

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, txt: str) -> None:
        if not isinstance(txt, str):
            raise ValueError("This need to be string")
        else:
            self._message = txt

    @property
    def rot_type(self) -> str:
        return self._rot_type

    @rot_type.setter
    def rot_type(self, txt: str) -> None:
        if not isinstance(txt, str):
            raise ValueError("This need to be string")
        else:
            self._rot_type = txt

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, txt: str) -> None:
        if not isinstance(txt, str):
            raise ValueError("This need to be string")
        else:
            self._status = txt

    @message.setter
    def message(self, txt: str) -> None:
        if not isinstance(txt, str):
            raise ValueError("This need to be string")
        else:
            self._message = txt

    def show_info(self) -> str:
        return (
            f"Message: {self._message}, Rot type: {self._rot_type}, "
            f"Status: {self._status}"
        )
