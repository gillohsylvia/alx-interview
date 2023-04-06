#!/usr/bin/python3

def minOperations(n):
    # checks if n is an integer
    if not isinstance(n, int):
        return 0

    #Divides n by iteration, effectively pasting iteratiom H characters.
    #Adds iteration to operation, keeping track of the total number of operations performed.
    #Sets iteration to 1, so that it will be incremented to 2 in the next iteration
    operation = 0
    iteration = 2
    while (iteration <= n):
        if not (n % iteration):
            n = int(n / iteration)
            operation += iteration
            iteration = 1
        # If n is not divisible by iteration, the loop simply increments iteration by 1.
        iteration += 1
    return operation

