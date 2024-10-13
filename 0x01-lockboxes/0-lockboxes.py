#!/usr/bin/python3
"""Lock Boxes"""


def canUnlockAll(boxes):
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for i in range(len(boxes)):
            boxes_checked = k in boxes[i] and k != i
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
