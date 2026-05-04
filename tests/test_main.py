import logging
import allure
import pytest

from penguin_tests.main import main

logger = logging.getLogger(__name__)


@allure.parent_suite("App 1")
@allure.suite("Main Suite")
@allure.sub_suite("Main Sub Suite")
@allure.tag("owner-jake")
@allure.tag("unit")
class TestMain:

    @allure.title("Foo some Tests Bar!")
    def test_foobar(self):
        assert True is True

    @pytest.mark.integration
    def test_main(self):
        assert main() == "Hello, World!"

    # @allure.suite("Main")a
    # @allure.sub_suite("Smoke")
    @pytest.mark.full
    def test_main_error(self):
        assert main() == "Hello, World!"
