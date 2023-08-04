#!/usr/bin/env python3

from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ The function uses a regex to replace
    occurrences of certain field values"""
    res = re.compile(r"({}=)([^{}]*)({})".format(
        "(?:{})".format("|".join(fields)), separator, separator))
    b = res.sub(r"\1{}\3".format(redaction), message)
    return b
