#!/usr/bin/env python3
"""Module Three Create logger"""

import re
from typing import List
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Update the class to accept a list of strings
            fields constructor argument.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Implement the format method to filter values in incoming log records
            using filter_datum. Values for fields in fields should be filtered.
            DO NOT extrapolate FORMAT manually. The format method should be
            less than 5 lines long.
        """
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(
            self.fields, self.REDACTION, original_message, self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """Implement a get_logger function that takes no arguments and
        returns a logging.Logger object.
        The logger should be named "user_data" and only log up to logging.INFO
        level. It should not propagate messages to other loggers. It should
        have a StreamHandler with RedactingFormatter as formatter.
        Create a tuple PII_FIELDS constant at the root of the module containing
        the fields from user_data.csv that are considered PII. PII_FIELDS can
        contain only 5 fields - choose the right list of fields that can are
        considered as “important” PIIs or information that you must hide in
        your logs. Use it to parameterize the formatter
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger
