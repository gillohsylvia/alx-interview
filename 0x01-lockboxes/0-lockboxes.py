#!/usr/bin/python3
#  method that determines if all the boxes can be opened.

def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True
    keys = boxes[0]

    for key in keys:
        if key < num_boxes and not unlocked_boxes[key]:
            unlocked_boxes[key] = True
            keys += boxes[key]

    return all(unlocked_boxes)

