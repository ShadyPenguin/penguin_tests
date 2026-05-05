from logging import getLogger

logger = getLogger(__name__)


def main():
    dog = "woof"
    global cat
    cat = "meow"
    logger.info("Main function called")
    try:
        raise Exception("Bad stuff")
    except Exception as e:
        logger.error(e)
    return "Hello, World!"
