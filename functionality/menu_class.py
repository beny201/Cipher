class Menu:
    def __init__(self) -> None:
        self.actions = {
            1: "Encryption",
            2: "Decryption",
            3: "Show all messages",
            4: "Save messages to file",
            5: "Open saved file",
            6: "Close program"
        }
        self.actions_submenu = {
            1: "Rot 13",
            2: "Rot 47",
        }

    def show(self) -> None:
        print("-" * 20)
        print("MENU:")
        for key, action in self.actions.items():
            print(f"{key}. {action}")
        print("-" * 20)

    def show_submenu(self) -> None:
        print("-" * 20)
        print("Please chose which cipher to use:")
        for key, action in self.actions_submenu.items():
            print(f"{key}. {action}")
        print("-" * 20)
