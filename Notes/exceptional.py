import sys
from math import log

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def convert_FAILED_AT_INT(s):
    """
        Failed first implementation of conversion method
        attempts to convert string to integer but fails when value can't
        be coerced into an integer
        e.g. convert(['lksjdflkj'])
    """
    number = ''
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number) 
    return x


def convert_FAILED_AT_ITERATION(s):
    """
        Failed second implementation of conversion method
        attempts to iterate through uniterable object and fails
        - e.g. convert(123)
    """
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except KeyError:
        x = -1
    return x


# def convert(s):
#     try:
#         number = ''
#         for token in s:
#             number += DIGIT_MAP[token]
#         x = int(number)
#     except KeyError:
#         x = -1
#     except TypeError:
#         print('Conversion Failed!')
#         x = -1
#     return x

def convert(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}", file=sys.stderr)
        pass # no-op, handles indentation error but continues on
    return x


def string_log(s):
    v = convert(s)
    return log(v)

