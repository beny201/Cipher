from abc import ABC, abstractmethod


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
            a = "a"
        elif c.isupper():
            a = "A"
        else:
            return c
        return chr(ord(c) + 13) if ord(c) < ord(a) + 13 else chr(ord(c) - 13)

    def rot(self) -> str:
        encrypted = "".join(self.rot_c(c) for c in self._message)
        return encrypted


class Rot47(Rot):
    def __init__(self, message: str = "None"):
        self._message = message

    @staticmethod
    def rot_c(c: str) -> str:
        if ord(c) < 33 or ord(c) > 127:
            return c
        return chr(ord(c) + 47) if ord(c) + 47 < 127 else chr(ord(c) - 47)

    def rot(self) -> str:
        encrypted = "".join(self.rot_c(c) for c in self._message)
        return encrypted
