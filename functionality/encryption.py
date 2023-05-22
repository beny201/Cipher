from dataclasses import dataclass
from typing import Optional
from abc import ABC, abstractmethod


@dataclass
class Text:
    _message: str = "Empty"
    _rot_type: Optional[str] = None
    _status: str = "decrypted"

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, txt: str) -> None:
        if not isinstance(txt, str):
            raise ValueError("This need to be string")
        else:
            self._message = txt

    @property
    def rot_type(self):
        return self._rot_type

    @rot_type.setter
    def rot_type(self, txt: str) -> None:
        if not isinstance(txt, str):
            raise ValueError("This need to be string")
        else:
            self._rot_type = txt

    @property
    def status(self):
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

    def show_info(self):
        return (f"Message: {self._message}, Rot type: {self._rot_type}, "
                f"Status: {self._status}")


class Rot(ABC):
    @staticmethod
    def rot_c(c: str):
        pass

    @abstractmethod
    def rot(self):
        pass


class Rot13(Rot):
    def __init__(self, message: str = "None"):
        self._message = message

    @staticmethod
    def rot_c(c: str) -> str:
        if c.islower():
            a = 'a'
        elif c.isupper():
            a = 'A'
        else:
            return c
        return chr(ord(c) + 13) if ord(c) < ord(a) + 13 else chr(ord(c) - 13)

    def rot(self):
        encrypted = ''.join(self.rot_c(c) for c in self._message)
        return encrypted


class Rot47(Rot):
    def __init__(self, message: str = "None"):
        self._message = message

    @staticmethod
    def rot_c(c: str) -> str:
        if ord(c) < 33 or ord(c) > 127:
            return c
        return chr(ord(c) + 47) if ord(c) + 47 < 127 else chr(ord(c) - 47)

    def rot(self):
        encrypted = ''.join(self.rot_c(c) for c in self._message)
        return encrypted


def main():
    objet2 = Text("asdasd")
    obiekt2 = Rot47("text")
    print(obiekt2.rot())


if __name__ == "__main__":
    main()
