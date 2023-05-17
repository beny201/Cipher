import json


def saving_file(name: str, data) -> None:
    try:
        with open(f"{name}.json", "r") as f:
            file_exist = True
    except FileNotFoundError:
        file_exist = False
    try:
        with open(f"{name}.json", "a" if file_exist else "w") as file:
            file.write(f"{data}")
    except FileNotFoundError:
        print("Seems there is issue with saving")


def reading_file(name: str) -> str:
    try:
        with open(f"{name}.json", "r") as file:
            data = file.readline()
            return data
    except FileNotFoundError:
        print("There is no file with this name ")
