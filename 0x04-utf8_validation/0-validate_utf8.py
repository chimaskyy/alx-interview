#!/usr/bin/python3
"""this script determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:

        mask_byte = 1 << 7

        if number_bytes == 0:
            '''Count the number of leading 1s in the
            byte to determine the number of bytes'''
            while mask_byte & byte:
                number_bytes += 1
                mask_byte >>= 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            # Check that the byte is a valid continuation byte
            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
