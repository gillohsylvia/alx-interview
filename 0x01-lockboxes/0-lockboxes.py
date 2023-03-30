#!/usr/bin/python3
"""
Implement lockboxes
"""


def canUnlockAll(boxes):

    """
    Takes a list of lists as an argument and where each box contains the key
    to the any other box, the first box is unloack by default
    """

    obj = {}
    if len(boxes) <= 0:
        return False
    for box in range(len(boxes)):
        can_unlock = False
        # print('Box ', box)
        if box > 0 and box not in obj.keys():
            for key, value in obj.items():
                # print(box)
                # if key == box and value == 'unlocked':
                if box in boxes[key]:
                    # print('here')
                    can_unlock = True
                    break
            if not can_unlock:
                return False
            continue
        keys = boxes[box]
        for key in range(len(keys)):
            if keys[key] < len(boxes):
                # checks if key is a valid box index
                # add the key as the 'key' to the object, obj
                element = keys[key]
                obj[element] = 'unlocked'
            else:
                obj[element] = 'locked'
    return True
