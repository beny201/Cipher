from typing import List, Dict
from functionality.text import Text
from dataclasses import asdict


class Buffer:
    def __init__(self):
        self.temporary_container: List[Text] = []

    def data_for_saving(self) -> List[Dict]:
        return [asdict(text) for text in self.temporary_container]

    def read_contents(self) -> None:
        if len(self.temporary_container) >= 1:
            print()
            for i, text in enumerate(self.temporary_container, start=1):
                print(f"{i}. {text.show_info()}")
        else:
            print("Container is empty")

    def append_text(self, message: Text) -> None:
        self.temporary_container.append(message)

    def user_action(self) -> int:
        while True:
            user_input = input("Please write position to remove: ")
            try:
                user_choice = int(user_input)
                if user_choice > len(self.temporary_container):
                    raise ValueError
                else:
                    return int(user_input) - 1
            except ValueError:
                print("Please write valid number")

    def remove_message(self, position_to_remove: int) -> None:
        self.temporary_container.pop(position_to_remove)

    def remove_text(self) -> None:
        user_choice_to_remove = self.user_action()
        self.remove_message(user_choice_to_remove)
