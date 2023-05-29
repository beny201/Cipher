import os
import json

from functionality.file_handler import saving_file, reading_file


def test_should_read_file(mocker):
    test_dict = [{"_message": "Mati", "_rot_type": "Rot47", "_status": "Decrypted"}]

    with open("file_test.json", "w+") as json_file:
        json.dump(test_dict, json_file, indent=4)

    mock_file_path = "file_test"
    name = "not_needed"
    mocker.patch("functionality.file_handler.os.path.join", return_value=mock_file_path)
    expected = [{"_message": "Mati", "_rot_type": "Rot47", "_status": "Decrypted"}]
    assert reading_file(name) == expected
    os.remove("file_test.json")


def test_should_create_file(mocker):
    mock_file_path = "file_test_1"
    name = "not_needed"
    mocker.patch("functionality.file_handler.os.path.join", return_value=mock_file_path)
    data = [{"_message": "Mati", "_rot_type": "Rot47", "_status": "Decrypted"}]
    saving_file(name, data)
    with open(f"{mock_file_path}.json", "r") as json_file:
        saved_data = json.load(json_file)
        assert saved_data == data
    os.remove("file_test_1.json")


def test_should_add_data_to_file_if_exist(mocker):
    mock_file_path = "file_test_2"
    name = "not_needed"
    mocker.patch("functionality.file_handler.os.path.join", return_value=mock_file_path)
    data = [{"_message": "Mati", "_rot_type": "Rot47", "_status": "Decrypted"}]
    saving_file(name, data)
    saving_file(name, data)
    with open(f"{mock_file_path}.json", "r") as json_file:
        saved_data = json.load(json_file)
        assert saved_data[1] == data[0]
    os.remove("file_test_2.json")
