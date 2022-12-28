import pytest
import typing as t

from athenaeum.utils import handle_args


class TestHandleArgs:
    @pytest.mark.parametrize(["expected", "arg", "args"], [
        pytest.param((None,), None, tuple(), id="handle_args(None)"),
        pytest.param((1,), 1, tuple(), id="handle_args(1)"),
        pytest.param(('a',), 'a', tuple(), id="handle_args('a')"),
        pytest.param(('abc',), 'abc', tuple(), id="handle_args('abc')"),
        pytest.param(('a', 'b', 'c'), 'a', ('b', 'c'), id="handle_args('a', 'b', 'c')"),
        pytest.param(('a', 'bc'), 'a', ('bc',), id="handle_args('a', 'bc')"),
        pytest.param((1, 2, 3), 1, (2, 3), id="handle_args(1, 2, 3)"),
        pytest.param((1, 2, 3), [1, 2, 3], tuple(), id="handle_args([1, 2, 3])"),
        pytest.param(({},), {}, tuple(), id="handle_args({})"),
        pytest.param(({'a': 1},), {'a': 1}, tuple(), id="handle_args({'a': 1})"),
        pytest.param((1, [1, 2, 3]), 1, ([1, 2, 3],), id="handle_args(1, [1, 2, 3])")
    ])
    def test(self, expected, arg, args):
        result1 = handle_args(arg, args)
        result2 = handle_args(arg, *args)
        result3 = handle_args(arg) + args

        assert expected == result1 == result2 == result3

    @pytest.mark.parametrize(["expected", "num", "nums"], [
        pytest.param(3, 1, (2,), id="summation(1, 2)"),
        pytest.param(3, [1, 2], tuple(), id="summation([1, 2])")
    ])
    def test_summation(self, summation: callable, expected: int, num: t.Union[int, t.Sequence], nums: t.Sequence):
        result = summation(num, *nums)

        assert expected == result
