import pytest
from encryption_software.encryption import *


@pytest.mark.parametrize("txt, expected", [("a", "n"), ("T", "G")])
def test_should_return_char_for_rot13c(txt, expected):
    text_object = Text(txt)
    assert text_object.rot13c(txt) == expected


@pytest.mark.parametrize("txt, expected", [(
        "this is check, question? ",
        "guvf vf purpx, dhrfgvba? "), (
        "guvf vf purpx, dhrfgvba?",
        "this is check, question?")])
def test_should_return_sentence_for_rot13(txt, expected):
    text_object = Text(txt)
    assert text_object.rot13() == expected


@pytest.mark.parametrize("txt, expected", [("!", "P"), ("~", "O"), ("5", "d")])
def test_should_return_char_for_rot47c(txt, expected):
    text_object = Text(txt)
    assert text_object.rot47c(txt) == expected


@pytest.mark.parametrize("txt, expected", [(
        "To zdanie jest zakodowane.", "%@ K52?:6 ;6DE K2<@5@H2?6]"),
    ("%@ K52?:6 ;6DE K2<@5@H2?6]",
     "To zdanie jest zakodowane.")])
def test_should_return_sentence_for_rot47(txt, expected):
    text_object = Text(txt)
    assert text_object.rot47() == expected
