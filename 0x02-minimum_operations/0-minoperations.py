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
 
def isPrime(n):
    """
    Checks if n is a prime number
    """

    for i in range(2, (n // 2)):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    """
    Returns all the prime factors of the number n
    """
    factors = []
    # for i in range(2, (n//2)):
    for i in range(2, int(n**0.5+1)):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors


def minOperations(n):
    """
    Returns an Integer which indicates the fewest number of opertions to get
    the n of H character in the file given the minimal type of operations
    allowable
    """
    if n <= 1:
        return 0
    sum = 0
    for i in prime_factors(n):
        sum += i
    return sum