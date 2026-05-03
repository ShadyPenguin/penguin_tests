import pytest

from penguin_tests import failure


def test_failure():
    assert failure.return_false() is False


def test_error():
    failure.throw_exception()
    assert False


@pytest.mark.skip("This test is skipped")  # pyright: ignore[reportUndefinedVariable]
def test_skip():
    assert False
