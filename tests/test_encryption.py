import pytest
from functionality.encryption import Rot13, Rot47


@pytest.mark.parametrize("txt, expected", [("a", "n"), ("T", "G")])
def test_should_return_char_for_rot13c(txt, expected):
    text_object = Rot13(txt)
    assert text_object.rot_c(txt) == expected


@pytest.mark.parametrize(
    "txt, expected",
    [
        ("this is check, question? ", "guvf vf purpx, dhrfgvba? "),
        ("guvf vf purpx, dhrfgvba?", "this is check, question?"),
    ],
)
def test_should_return_sentence_for_rot13(txt, expected):
    text_object = Rot13(txt)
    assert text_object.rot() == expected


@pytest.mark.parametrize("txt, expected", [("!", "P"), ("~", "O"), ("5", "d")])
def test_should_return_char_for_rot47c(txt, expected):
    text_object = Rot47(txt)
    assert text_object.rot_c(txt) == expected


@pytest.mark.parametrize(
    "txt, expected",
    [
        ("To zdanie jest zakodowane.", "%@ K52?:6 ;6DE K2<@5@H2?6]"),
        ("%@ K52?:6 ;6DE K2<@5@H2?6]", "To zdanie jest zakodowane."),
    ],
)
def test_should_return_sentence_for_rot47(txt, expected):
    text_object = Rot47(txt)
    assert text_object.rot() == expected
