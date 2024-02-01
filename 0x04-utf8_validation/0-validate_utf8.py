#!/usr/bin/python3
"""Valid UTF-8 Module"""


def validUTF8(data):
    """method that determines if a given data
    set represents a valid UTF-8 encoding"""
    bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:
        mask_byte = 1 << 7
        if bytes == 0:
            while mask_byte & i:
                bytes += 1
                mask_byte = mask_byte >> 1
            if bytes == 0:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False
        bytes -= 1
    return bytes == 0
