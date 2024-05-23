#!/usr/bin/python3
"""This script checks if n number of locked boxes
numbered sequentially from 0 to n - 1 can all be
opened and each box may contain keys to
the other boxes."""


def canUnlockAll(boxes):
    """Determines if all the boxes can be unlocked.
    
    Args:
        boxes (list of lists): List where each index represents a box and
                               contains a list of keys to other boxes.
                               
    Returns:
        bool: True if all boxes can be unlocked, else False.
    """
    
    # Start with the first box's key
    keys = [0]
    unlocked = set(keys)  # Set to track unlocked boxes
    
    # Iterate over keys we have
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey < len(boxes) and boxKey not in unlocked:
                unlocked.add(boxKey)
                keys.append(boxKey)
                
    # Check if we have unlocked all boxes
    return len(unlocked) == len(boxes)
