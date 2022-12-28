import pytest

from athenaeum.utils import handle_args


@pytest.fixture
def summation() -> callable:
    def _summation(num: int, *nums: tuple) -> int:
        numbers = handle_args(num, nums)

        return sum(numbers)
    return _summation
