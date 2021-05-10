# Adapted from https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output

import logging
import os

RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"

def message_format(message,color):
    if color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

FORMAT = "%(asctime)s [$BOLD %(name)s $RESET][ %(levelname)s ] %(message)s (%(filename)s:%(lineno)d)"
COLOR_FORMAT = message_format(FORMAT, True)


COLORS = {
    'WARNING': YELLOW,
    'INFO': BLUE,
    'DEBUG': WHITE,
    'CRITICAL': RED,
    'ERROR': RED
}

class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color = True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            levelname_color = COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
            record.levelname = levelname_color
            record.msg = COLOR_SEQ % (30+COLORS[levelname]) + record.msg + RESET_SEQ
        return logging.Formatter.format(self, record)


def setup_logging(level="INFO"):
    color_formatter = ColoredFormatter(COLOR_FORMAT)
    h = logging.StreamHandler(None)
    h.setFormatter(color_formatter)
    logging.root.addHandler(h)
    logging.root.setLevel(os.environ.get("LOGLEVEL", level))





if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")