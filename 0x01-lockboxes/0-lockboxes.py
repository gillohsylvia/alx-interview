#!/usr/bin/python3
"""
Contains a function called canUnlockAll
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """
    keys = set()

    for box_id, box in enumerate(boxes):
        if len(box) == 0 or box_id == 0:
            keys.add(box_id)
        for key in box:
            if key < len(boxes) and key != box_id:
                keys.add(key)
        if len(keys) == len(boxes):
            return True
    return False
