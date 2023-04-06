#!/usr/bin/python3

def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor can execute
    only two operations in this file: Copy All and Paste. Given a number n,
    write a method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.

    Returns an integer
    If n is impossible to achieve, returns 0
    """
    if not isinstance(n, int):
        return 0

    operation = 0
    iteration = 2
    while iteration <= n:
        if not (n % iteration):
            n = int(n / iteration)
            operation += iteration
            iteration = 1
        iteration += 1
    return operation
