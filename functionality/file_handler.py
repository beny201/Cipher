import json
import os.path
from typing import List


def saving_file(name: str, data: List[dict]) -> None:
    folder = "json_files"
    file_path = os.path.join(folder, name)
    try:
        with open(f"{file_path}.json", "r") as f:
            file_exist = True
    except FileNotFoundError:
        file_exist = False
    try:
        if file_exist:
            with open(f"{file_path}.json", "r+") as json_file:
                existing_data = json.load(json_file)
                for files in data:
                    existing_data.append(files)
            with open(f"{file_path}.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)
        else:
            with open(f"{file_path}.json", "a") as json_file:
                data_to_save = data
                json.dump(data_to_save, json_file, indent=4)
    except FileNotFoundError:
        print("Seems there is issue with saving")


def reading_file(name: str) -> List[dict]:
    folder = "json_files"
    file_path = os.path.join(folder, name)
    with open(f"{file_path}.json", "r") as json_file:
        data = json.load(json_file)
        return data
