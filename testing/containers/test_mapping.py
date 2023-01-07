import typing as t
import pytest

from athenaeum.containers import Mapping


class TestMapping:
    @pytest.mark.parametrize(["expected", "mapping"], [
        pytest.param({}, {}, id="empty_dict"),
        pytest.param({"alpha": "a"}, {"a": "alpha"}),
        pytest.param({0: "alpha", 1: "alpha", "a": "beta", "b": "beta"}, {"alpha": [0, 1], "beta": ["a", "b"]})
    ])
    def test_invert(self, expected: t.Mapping, mapping: t.Mapping):
        assert expected == Mapping.invert(mapping)
