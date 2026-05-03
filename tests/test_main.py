from penguin_tests.main import main


def test_main():
    assert main() == "Hello, World!"


if __name__ == "__main__":
    test_main()
