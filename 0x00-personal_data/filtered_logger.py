#!/usr/bin/env python3

"""This module contains code for the
alx personal data task in the alx backend specialisation
"""

import logging
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Uses a regex to replace occurrences of certain field values"""
    pattern = r"({}=)([^{}]*)({})".format(
        "(?:{})".format("|".join(fields)), separator, separator)
    return re.sub(pattern, r"\1{}\3".format(redaction), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """Constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the redacted logs"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)
