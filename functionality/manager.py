from typing import List, Dict
from functionality.menu import Menu
from functionality.buffer import Buffer
from functionality.encryption import Rot13, Rot47
from functionality.text import Text
from functionality.file_handler import saving_file, reading_file


class Manager:
    available_rots = {1: (Rot13, "Rot13"), 2: (Rot47, "Rot47")}

    def __init__(self) -> None:
        self._is_running = True
        self.menu = Menu()
        self.rot13 = Rot13()
        self.rot47 = Rot47()
        self.buffer = Buffer()

        self.action_main = {
            1: self.process_encryption,
            2: self.process_decryption,
            3: self.buffer.read_contents,
            4: self.buffer.remove_text,
            5: self.saving_file_manager,
            6: self.reading_file_manager,
            7: self.finish,
        }

    def run(self) -> None:
        while self._is_running:
            self.menu.show()
            user_choice = self.user_choice_action()
            self.execute_main(user_choice)

    @staticmethod
    def user_choice_action() -> int:
        while True:
            user_input = input("Please write number of desired actions: ")
            try:
                user_choice = int(user_input)
                return user_choice
            except ValueError:
                print("Please write valid number")

    @staticmethod
    def get_user_message() -> str:
        user_choice = input("Please write message: ")
        return user_choice

    @staticmethod
    def get_user_file_name() -> str:
        user_choice = input("Please write name of file: ")
        return user_choice

    def process_encryption(self) -> None:
        self.menu.show_submenu()
        user_choice = self.user_choice_action_validation_sub_menu()
        user_message_to_encrypt = self.get_user_message()
        message_to_stock = self.encryption(user_choice, user_message_to_encrypt)
        self.buffer.append_text(message_to_stock)

    def process_decryption(self) -> None:
        self.menu.show_submenu()
        user_choice = self.user_choice_action_validation_sub_menu()
        user_message_to_decrypt = self.get_user_message()
        message_to_stock = self.decryption(user_choice, user_message_to_decrypt)
        self.buffer.append_text(message_to_stock)

    def user_choice_action_validation_sub_menu(self) -> int:
        check_on = True
        while check_on:
            scope = len(self.menu.actions_submenu)
            try:
                user_choice = self.user_choice_action()
                if user_choice > scope or user_choice <= 0:
                    raise ValueError()
                else:
                    check_on = False
                    return user_choice
            except ValueError:
                print(f"This need to be from 1 to {scope}")

    @staticmethod
    def encryption(user_choice: int, message_to_encrypt: str) -> Text | None:
        rot = Manager.available_rots.get(user_choice)
        if rot is not None:
            rot_obj, rot_type = rot
            encrypted_message = rot_obj(message_to_encrypt).rot()
            message_to_stock = Text(encrypted_message, rot_type, "Encrypted")
            print(f"Encrypted: {encrypted_message} - This will be stocked")
            return message_to_stock

    @staticmethod
    def decryption(user_choice: int, message_to_decrypt: str) -> Text:
        rot = Manager.available_rots.get(user_choice)
        if rot is not None:
            rot_obj, rot_type = rot
            encrypted_message = rot_obj(message_to_decrypt).rot()
            message_to_stock = Text(encrypted_message, rot_type, "Decrypted")
            print(f"Encrypted: {encrypted_message} - This will be stocked")
            return message_to_stock

    def execute_main(self, user_choice: int) -> None:
        if user_choice in self.action_main.keys():
            return self.action_main[user_choice]()
        else:
            print(f"Please chose no from range 1 - {len(self.action_main)}")

    def saving_file_manager(self) -> None:
        name_file = self.get_user_file_name()
        files_to_save = self.buffer.data_for_saving()
        saving_file(name_file, files_to_save)

    def reading_file_manager(self) -> None:
        data_to_read = self.reading_file_to_convert()
        self.converting_saved_files_to_text(data_to_read)

    def reading_file_to_convert(self) -> List[dict]:
        check_on = True
        while check_on:
            name_file = self.get_user_file_name()
            try:
                data = reading_file(name_file)
                return data
            except FileNotFoundError:
                print("Seems there is no file")

    def converting_saved_files_to_text(self, file: List[dict]) -> None:
        for data in file:
            message = data["_message"]
            rot_type = data["_rot_type"]
            status = data["_status"]
            self.buffer.append_text(Text(message, rot_type, status))

    def finish(self) -> None:
        possibility_to_save = input("Do you want to save before exit? Y/N: ")
        if possibility_to_save.lower() == "y":
            self.saving_file_manager()
        else:
            self._is_running = False
