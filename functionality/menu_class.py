class Menu:
    def __init__(self) -> None:
        self.actions = {
            1: "Encryption",
            2: "Decryption",
            3: "Show all messages",
            4: "Remove message from stock",
            5: "Save messages to file",
            6: "Open saved file",
            7: "Close program"
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

def main():
    obiekt1 = Menu()
    print(len(obiekt1.actions_submenu))
    #obiekt3 = Text("asdasd")
    #obiekt1.buffer.append_text(obiekt3)
    #zapis = obiekt1.buffer.data_for_saving()

    #obiekt1.procces_encrytpion()
    #obiekt1.buffer.read_contents()
    #saving_file("marian", *zapis)
    #data = reading_file("marian")
    #print(data)

if __name__ == "__main__":
    main()
