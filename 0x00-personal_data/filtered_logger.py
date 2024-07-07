#!/usr/bin/env python3
"""Module One Regexing"""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Write a function called filter_datum
        that returns the log message obfuscated:
    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is
        separating all fields in the log line (message)
    Return:
        The function should use a regex to replace
        occurrences of certain field values.
        filter_datum should be less than 5 lines long and use re.sub
        to perform the substitution with a single regex.
    """
    escaped_fields = map(re.escape, fields)
    joined_fields = '|'.join(escaped_fields)
    escaped_separator = re.escape(separator)
    pattern = r'({})=(.*?){}'.format(joined_fields, escaped_separator)
    return re.sub(pattern, r'\1={}{}'.format(redaction, separator), message)
