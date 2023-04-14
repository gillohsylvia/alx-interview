#!/usr/bin/python3
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

def minOperations(n):
    '''
    alculates the fewest number of operations needed to
    result in exactly n H characters
    '''
    if n <= 1:  # If n is impossible to achieve
        return 0
    num_operations = 0  # number of operations required
    i = 2  # initialize i to the smallest prime factor
    # Divide n by its prime factors, starting with the smallest prime factor
    while i <= n:
        if n % i == 0:
            n //= i
            num_operations += i
            i = 2  # reset the value of i
        else:
            i += 1
    return num_operations