from dataclasses import dataclass
# from buffer import *

@dataclass
class Text:
    _message: str

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, txt):
        if not isinstance(txt, str):
            raise ValueError("This need to be string")
        else:
            self._message = txt

    @staticmethod
    def rot13c(c):
        if c.islower():
            a = 'a'
        elif c.isupper():
            a = 'A'
        else:
            return c
        return chr(ord(c) + 13) if ord(c) < ord(a) + 13 else chr(ord(c) - 13)

    def rot13(self):
        encrypted = ''.join(Text.rot13c(c) for c in self.message)
        return encrypted

    @staticmethod
    def rot47c(c):
        if ord(c) < 33 or ord(c) > 127:
            return c
        return chr(ord(c) + 47) if ord(c) + 47 < 127 else chr(ord(c) - 47)

    def rot47(self):
        encrypted = ''.join(Text.rot47c(c) for c in self.message)
        return encrypted

