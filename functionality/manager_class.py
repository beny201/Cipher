from menu_class import Menu
from buffer import Buffer
from encryption import Text, Rot13, Rot47
from file_handler import saving_file, reading_file


class Manager:
    def __init__(self) -> None:
        self.working = True
        self.menu = Menu()
        self.rot13 = Rot13()
        self.rot47 = Rot47()
        self.buffer = Buffer()

        self.action_main = {
            1: self.process_encryption,
            2: self.process_decryption,
            3: self.buffer.read_contents,
            4: self.saving_file_manager,
            5: self.reading_file_manager,
            6: self.finish
        }

    def run(self) -> None:
        while self.working:
            self.menu.show()
            user_choice = self.user_choice_action()
            self.execute_main(user_choice)

    @staticmethod
    def user_choice_action() -> int:
        while True:
            user_input = input("Please write what do you want to do: ")
            try:
                user_choice = int(user_input)
                return user_choice
            except ValueError:
                print("Please write valid number")

    @staticmethod
    def user_message() -> str:
        user_choice = (input("Please write message: "))
        return user_choice

    @staticmethod
    def user_name_file() -> str:
        user_choice = (input("Please write name of file: "))
        return user_choice

    def process_encryption(self):
        self.menu.show_submenu()
        user_choice = self.user_choice_action_validation_sub_menu()
        user_message_to_encrypt = self.user_message()
        message_to_stock = self.encryption(user_choice,
                                           user_message_to_encrypt)
        self.buffer.append_text(message_to_stock)

    def user_choice_action_validation_sub_menu(self):
        check_on = True
        while check_on:
            scope = len(self.menu.actions_submenu) + 1
            try:
                user_choice = self.user_choice_action()
                if user_choice >= scope or user_choice <= 0:
                    raise ValueError()
                else:
                    check_on = False
                    return user_choice
            except ValueError:
                print((f"This need to be from 1 to {scope}"))

    def encryption(self, user_choice, message_to_encrypt):
        if user_choice == 1:
            encrypted_message = Rot13(message_to_encrypt).rot()
            message_to_stock = Text(encrypted_message, "Rot13", "Encrypted")
            print(f"Encrypted: {encrypted_message}/ This will be stocked")
            return message_to_stock
        elif user_choice == 2:
            encrypted_message = Rot47(message_to_encrypt).rot()
            message_to_stock = Text(encrypted_message, "Rot47", "Encrypted")
            print(f"Encrypted: {encrypted_message}/ This will be stocked")
            return message_to_stock
        else:
            print(
                f"Please chose no from range 1 - {len(self.menu.actions_submenu)}")

    def process_decryption(self):
        pass

    def execute_main(self, user_choice: int):
        if user_choice in self.action_main.keys():
            return self.action_main[user_choice]()
        else:
            print(f"Please chose no from range 1 - {len(self.action_main)}")

    def saving_file_manager(self):
        name_file = self.user_name_file()
        files_to_save = self.buffer.data_for_saving()
        print(files_to_save)
        saving_file(name_file, files_to_save)

    def reading_file_manager(self):
        pass

    def finish(self):
        self.working = False


def main():
    obiekt1 = Manager()
    obiekt1.run()
    # obiekt3 = Text("asdasd")
    # obiekt1.buffer.append_text(obiekt3)
    # zapis = obiekt1.buffer.data_for_saving()

    # obiekt1.procces_encrytpion()
    # obiekt1.buffer.read_contents()
    # saving_file("marian", *zapis)
    # data = reading_file("marian")
    # print(data)


if __name__ == "__main__":
    main()
