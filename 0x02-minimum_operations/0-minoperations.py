#!/usr/bin/python3

""" 0x02. Minimum Operations """


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

    op = 0
    a = 2
    while (a <= n):
        if not (n % a):
            n = int(n / a)
            op += a
            a = 1
        a += 1
    return op
