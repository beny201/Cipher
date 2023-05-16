class Menu:
    def __init__(self) -> None:
        self.actions = {
            1: ""
        }

    def show(self) -> None:
        print("-"*10)
        print("Menu:")
        for key, action in self.actions.items():
            print(f"{key}. {action}")
        print("-" * 10)
