#!/usr/bin/env python3

"""This module contains code for the
alx personal data task in the alx backend specialisation
"""

from typing import List
import logging
import re

PII_FIELDS = ("name", "email", "phone", "password", "ssn")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Uses a regex to replace occurrences of certain field values"""
    pattern = r"({}=)([^{}]*)({})".format(
        "(?:{})".format("|".join(fields)), separator, separator)
    return re.sub(pattern, r"\1{}\3".format(redaction), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the redacted logs"""
        message = super().format(record)
        redacted_log = filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR)
        return redacted_log


def get_logger() -> logging.Logger:
    """Returns a new logger
    """
    logger = logging.Logger(name="user_data", level=logging.INFO)
    logger.propagate = False
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger
