import logging
import allure
import pytest

from penguin_tests.main import main

logger = logging.getLogger(__name__)


@allure.parent_suite("Main Parent Suite")
@allure.suite("Main Suite")
@allure.sub_suite("Main Sub Suite")
class TestMain:
    # @pytest.fixture(scope="module", autouse=True)
    # def before_each():
    #     allure.dynamic.parent_suite("'Main' Tests")
    #     allure.dynamic.sub_suite("Jake")
    #     allure.dynamic.label("owner", "Jake")
    #     logger.error("oops")
    #     yield

    @allure.title("Foo some Tests Bar!")
    def test_foobar(self):
        assert True is True

    # @allure.parent_suite("All Tests")
    # @allure.suite("Main")
    # @allure.sub_suite("Integration")
    def test_main(self):
        assert main() == "Hello, World!"

    # @allure.suite("Main")a
    # @allure.sub_suite("Smoke")
    # @pytest.mark.integration
    def test_main_error(self):
        assert main() == "Hello, World!"
