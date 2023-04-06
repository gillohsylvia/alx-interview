#!/usr/bin/python3

def minOperations(n):
    """
    step1 : checks if n is an integer
    step2 : if n is not an integer return 0
    step3 : if n is an integer operation set to zero
    step4: initialize variable i to 2 which will be used in the loop
    step5: checks if n can be divided by i.
    step6: if n is not divisible by i, i is incremented by one
    step7 : if n is divisible by i, n becomes the division of n and i
    step 8 : operation is incremented by i and i is set to 1
    step 9 : return operation when i becomes greater then n
    """

    if not isinstance(n, int):
        return 0

    op = 0
    i = 2
    while(i <= n):
        if not (n % i):
            n = int(n/i)
            op += i
        i += 1
    return op
