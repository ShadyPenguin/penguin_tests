import pytest
import allure

from penguin_tests import failure


@allure.parent_suite("Failiure Parent Suite")
@allure.suite("Failure Suite")
@allure.sub_suite("Failure Sub Suite")
class TestMain:
    def test_failure(self):
        assert failure.return_false() is False

    def test_error(self):
        failure.throw_exception()
        assert False

    @pytest.mark.skip(
        "This test is skipped"
    )  # pyright: ignore[reportUndefinedVariable]
    def test_skip(self):
        assert False
