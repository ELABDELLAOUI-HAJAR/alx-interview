#!/usr/bin/python3
"""Script that contains the method canUnlockAll"""


def canUnlockAll(boxes):
    """ Method that return True if all boxes can be opened,
    else return False
    """

    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True
