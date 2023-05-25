import pytest
from functionality.manager_class import *


def test_should_return_false(mocker):
    manager = Manager()
    mock_object = mocker.patch('builtins.input')
    mock_object.object.return_value = "n"
    manager.finish()
    assert manager.working == False


def test_should_add_text_to_list_from_saved_files():
    manager = Manager()
    buffer = Buffer()
    data = [{
        "_message": "Approve",
        "_rot_type": "Test",
        "_status": "Added"
    }]
    manager.converting_saved_files_to_text(data)
    assert len(manager.buffer.temporary_container) == 1
    message = manager.buffer.temporary_container[0]
    assert message.message == "Approve"
    assert message.rot_type == "Test"
    assert message.status == "Added"


def test_should_return_action():
    manager = Manager()

    def approve_action():
        return "Approve"

    manager.action_main = {
        1: approve_action
    }

    def approve_action():
        return "Approve"

    assert manager.execute_main(1) == "Approve"


def test_should_return_decrypted_message():
    manager = Manager()
    user_choice = 1
    message_to_encrypt = "guvf vf purpx, dhrfgvba?"
    expected = Text("this is check, question?", "Rot13", "Decrypted")
    assert manager.decryption(user_choice, message_to_encrypt) == expected
    user_choice = 2
    message_to_encrypt = "E9:D :D 4964<[ BF6DE:@?n"
    expected = Text("this is check, question?", "Rot47", "Decrypted")
    assert manager.decryption(user_choice, message_to_encrypt) == expected


def test_should_return_encrypted_message():
    manager = Manager()
    user_choice = 1
    message_to_encrypt = "guvf vf purpx, dhrfgvba?"
    expected = Text("this is check, question?", "Rot13", "Encrypted")
    assert manager.encryption(user_choice, message_to_encrypt) == expected
    user_choice = 2
    message_to_encrypt = "E9:D :D 4964<[ BF6DE:@?n"
    expected = Text("this is check, question?", "Rot47", "Encrypted")
    assert manager.encryption(user_choice, message_to_encrypt) == expected

