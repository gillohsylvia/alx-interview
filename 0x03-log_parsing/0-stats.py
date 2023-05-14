#!/usr/bin/python3
"""
1. Read input from the command line, line by line.
2. Verify the format of each line; if it doesn't match the expected format, move on to the next line.
3. Initialize a counter variable and increment it for every valid line.
4. Check if the counter reaches a value of 10; if it does, perform calculations.
5. Set up a dictionary to store status codes encountered during processing.
6. Create a variable to keep track of the file size.
7. With each line read, check if the corresponding key is present in the dictionary.
8. Update the file size accordingly.
9. Print the file size.
10. If either the key or the value is missing, continue to the next line; otherwise, print the corresponding status code."
"""
import sys


def parse_log():
    count = 0
    fileSize = 0
    pStatusCode = [200, 301, 400, 401, 403, 404, 405, 500]
    statusCodeOccurence = {}

    try:
        for line in sys.stdin:
            each = line.split()
            if len(each) < 2:
                return None
            count += 1
            fileSize += int(each[-1:][0])
            statusCode = int(each[-2:][0])
            if statusCode in pStatusCode:
                if statusCode in statusCodeOccurence:
                    statusCodeOccurence[statusCode] += 1
                else:
                    statusCodeOccurence[statusCode] = 1

            if count == 10:
                count = 0
                print_error(fileSize, statusCodeOccurence)
    except KeyboardInterrupt:
        print_error(fileSize, statusCodeOccurence)
        raise


def print_error(fileSize, statusCodeOccurence):
    print('File size: {}'.format(fileSize))
    for items in sorted(statusCodeOccurence.items()):
        print('{}: {}'.format(items[0], items[1]))


if __name__ == '__main__':
    parse_log()