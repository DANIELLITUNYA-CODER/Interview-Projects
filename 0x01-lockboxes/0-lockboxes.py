#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n  # Track which boxes have been unlocked
    unlocked[0] = True  # The first box is unlocked
    keys = [0]  # Start with the first box's keys

    while keys:
        current_box = keys.pop(0)  # Get the first key
        for key in boxes[current_box]:  # Check the keys in the current box
            if not unlocked[key]:  # If the box is not already unlocked
                unlocked[key] = True  # Unlock the box
                keys.append(key)  # Add the new key to the list

    return all(unlocked)  # Return True if all boxes are unlocked, otherwise False

# Example test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected output: False
