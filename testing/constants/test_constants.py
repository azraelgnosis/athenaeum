import pytest

from athenaeum.constants import Constant


@pytest.fixture
def coed_dict():
    return {
        "DERW": "derw",
        "MASARNEN": "masarnen",
    }


class Coed(object):
    class Consts(Constant):
        DERW = "derw"
        MASARNEN = "masarnen"


@pytest.fixture
def constant_class():
    class Coed(object):
        class Consts(Constant):
            DERW = "derw"
            MASARNEN = "masarnen"

    return Coed.Consts


class TestConstant:
    def test_iter(self, constant_class: Constant, coed_dict: dict):
        assert list(iter(constant_class)) == list(iter(coed_dict))

    def test_len(self, constant_class: Constant):
        assert len(constant_class) == 2

    def test_keys(self, constant_class: Constant, coed_dict: dict):
        assert constant_class.keys() == coed_dict.keys()

    def test_values(self, constant_class: Constant, coed_dict: dict):
        assert set(constant_class.values()) == set(coed_dict.values())

    def test_items(self, constant_class: Constant, coed_dict: dict):
        assert constant_class.items() == coed_dict.items()
