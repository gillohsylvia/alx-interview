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

    if n == 1:
        return 0   # This returns 0 if theres only 1 H.
    pf = 2  # Here we start with the lowest prime factor 2
    op = 0  # op Gets the number of operations

    while pf * pf <= n:
        if n % pf == 0:  # This checks for all the prime factors
            op += pf  # adds the factor to operations
            n //= pf  # This divides pf to reduce n for the next iteratio
        else:
            pf += 1   # if the number is not a factor, we increment.
    if n > 1:   # Adds the remaining prime factors of n
        op += n
    return op

    
