from logging import info

from penguin_tests.main import main


def test_main():
    info("Testing main function")
    assert main() == "Hello, World!"


def test_main_error():
    info("Testing main function error")
    assert main() == "Hello, World!"


if __name__ == "__main__":
    test_main()
