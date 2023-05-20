import json


def saving_file(name: str, data: dict) -> None:
    try:
        with open(f"{name}.json", "r") as f:
            file_exist = True
    except FileNotFoundError:
        file_exist = False
    try:
        if file_exist:
            with open(f"{name}.json", "r+") as json_file:
                existing_data = json.load(json_file)
                existing_data.append(data)
            with open(f"{name}.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)
        else:
            with open(f"{name}.json", "a") as json_file:
                data_to_save = data
                json.dump(data_to_save, json_file, indent=4)
    except FileNotFoundError:
        print("Seems there is issue with saving")


# jak to zrobic na dictcie? Nie udalo mi sie dodac dicta, wiec jest lista
def reading_file(name: str) -> str:
    try:
        with open(f"{name}.json", "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print("There is no file with this name ")
