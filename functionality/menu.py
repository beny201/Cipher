from typing import Dict


class Menu:
    def __init__(self) -> None:
        self.actions = {
            1: "Encryption",
            2: "Decryption",
            3: "Show all messages",
            4: "Remove message from stock",
            5: "Save messages to file",
            6: "Open saved file",
            7: "Close program",
        }
        self.actions_submenu = {
            1: "Rot 13",
            2: "Rot 47",
        }

    def __print_menu(self, title: str, action_dict: Dict[int, str]) -> None:
        print("-" * 20)
        print(title)
        for key, action in action_dict.items():
            print(f"{key}. {action}")
        print("-" * 20)

    def show(self) -> None:
        self.__print_menu("MENU", self.actions)

    def show_submenu(self) -> None:
        self.__print_menu("Please chose which cipher to use:", self.actions_submenu)
