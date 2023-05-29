from dataclasses import asdict

import pytest

from functionality.text import Text
from functionality.buffer import Buffer


@pytest.fixture
def set_object():
    buffer = Buffer()
    text_object = Text()
    buffer.append_text(text_object)
    return buffer, text_object


def test_should_return_dic(set_object):
    buffer, text_object = set_object
    assert buffer.data_for_saving() == [asdict(text_object)]
    buffer.append_text(text_object)
    assert buffer.data_for_saving() == [asdict(text_object), asdict(text_object)]


def test_should_add_object_to_list(set_object):
    buffer, text_object = set_object
    assert len(buffer.temporary_container) == 1
    assert text_object in buffer.temporary_container


def test_should_remove_object_from_list(set_object):
    buffer, text_object = set_object
    position = 0
    buffer.remove_message(position)
    assert len(buffer.temporary_container) == 0
    assert text_object not in buffer.temporary_container


def test_should_return_int_from_user_action(mocker):
    buffer = Buffer()
    text_object = Text()
    buffer.append_text(text_object)
    mocker.patch("builtins.input", return_value="1")
    assert buffer.user_action() == 0
