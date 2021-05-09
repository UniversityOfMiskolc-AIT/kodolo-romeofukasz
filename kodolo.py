# -*- coding: utf-8 -*-

"""String coder/encoder

Created by Romeo Ervin Fukasz (FY78UY).
"""

import sys
import argparse


def encode(input_string):
    """Encodes a string to comma seperated integers.

    Keyword arguments:
    input_string -- the string input to encode
    """

    if not isinstance(input_string, str):
        raise TypeError("The input of encode must be a string")

    if not input_string.isascii():
        raise ValueError("The input must only contain ascii characters")

    ascii_codes = [ord(char) for char in input_string]  # the ascii codes of the input's characters
    result_codes = [ascii_codes[0]]  # the first encoded number is the characters ascii code

    for index, value in enumerate(ascii_codes[1:], start=1):
        next_code_value = ascii_codes[index] - ascii_codes[index-1]
        result_codes.append(next_code_value)

    result_codes_as_strings = [str(element) for element in result_codes]
    result = ', '.join(result_codes_as_strings)
    return result


def string_is_integer(string):
    """Checks if the input string contains a valid integer value.

    Keyword arguments:
    string -- the input string to check if it contains a valid integer
    """

    if not isinstance(string, str):
        raise TypeError("The input of string_is_integer must be a string")

    is_unsigned_integer = string.isdigit()
    is_signed_integer = string[0] in ('-', '+') and string[1:].isdigit()
    return is_unsigned_integer or is_signed_integer


def decode(input_string):
    """Decodes comma seperated integers to the original string.

    Keyword arguments:
    input_string -- the string input to decode
    """

    if not isinstance(input_string, str):
        raise TypeError("The input of decode must be a string")

    list_of_string_elements = input_string.replace(" ", "").split(',')

    if not all([string_is_integer(element) for element in list_of_string_elements]):
        raise ValueError("Decoding input must be comma seperated integers")

    list_of_codes = [int(element) for element in list_of_string_elements]
    ascii_codes = [list_of_codes[0]]

    for code in list_of_codes[1:]:
        next_ascii_code = ascii_codes[-1] + code
        if not 0 <= next_ascii_code <= 127:
            raise ValueError("The input for decoding contains invalid numbers")
        ascii_codes.append(next_ascii_code)

    result = [chr(element) for element in ascii_codes]

    return "".join(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encode or decode strings for a good grade")
    parser.add_argument('--decode', dest='decode', action='store_true',
                        help='If this flag is set, the program decodes the input. Otherwise it encodes it.')
    parser.add_argument('input', nargs='+',
                        help='The input to be encoded or decoded. On encoding, the input may be any string '
                             'that only contains ascii characters. On decoding, the input must be comma seperated '
                             'integer values, eg.: 65,11,1,-12')
    args = parser.parse_args()

    user_input = ' '.join(args.input)  # merge input parameters into one string

    try:
        if args.decode:
            decoded_string = decode(user_input)
            print(decoded_string)
        else:
            encoded_string = encode(user_input)
            print(encoded_string)
    except (TypeError, ValueError) as e:
        print(f"An error occured: {e}", file=sys.stderr)
