from typing import List, Dict
from encryption import Text
from dataclasses import asdict


class Buffer:
    def __init__(self):
        self.temporary_container: List[Text] = []

    def data_for_saving(self) -> List[Dict]:
        dic_to_save = []
        for text in self.temporary_container:
            dic_to_save.append(asdict(text))
        return dic_to_save

    def read_contents(self):
        if len(self.temporary_container) >= 1:
            for text in self.temporary_container:
                print(text)
        else:
            print("Container is empty")

    def append_text(self, message: Text) -> None:
        self.temporary_container.append(message)


def main():
    objet2 = Buffer()

    #objet2.append_text(Text())
    #objet2.append_text(Text())
    #objet2.append_text(Text())
    objet2.read_contents()

if __name__ == "__main__":
    main()
