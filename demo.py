from text.logger import logging
from text.exception import CustomException
import sys

logging.info("Welcome to our project!")

try:

    a = 7 / "0"

except Exception as e:
    raise CustomException(e, sys) from e