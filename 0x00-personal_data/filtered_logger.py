#!/usr/bin/env python3

"""This module contains code for the
alx personal data task in the alx backend specialisation
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Uses a regex to replace occurrences of certain field values"""
    pattern = r"({}=)([^{}]*)({})".format(
        "(?:{})".format("|".join(fields)), separator, separator)
    return re.sub(pattern, r"\1{}\3".format(redaction), message)
