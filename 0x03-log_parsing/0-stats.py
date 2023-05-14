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

def parseLogs():
    """
    Reads logs from standard input and generates reports.
    Reports:
        * Prints the log size after reading every 10 lines and at KeyboardInterrupt.
    Raises:
        KeyboardInterrupt (Exception): Handles this exception and raises it.
    """
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')

    try:
        for line in iter(input, ''):
            lineNumber += 1
            log_parts = line.split()
            if len(log_parts) < 3:
                continue

            try:
                fileSize += int(log_parts[-1])
                status_code = log_parts[-2]
                if status_code in codes:
                    statusCodes[status_code] = statusCodes.get(status_code, 0) + 1
            except (IndexError, ValueError):
                continue

            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0

        report(fileSize, statusCodes)

    except KeyboardInterrupt:
        report(fileSize, statusCodes)
        raise

def report(fileSize, statusCodes):
    """
    Prints the generated report to standard output.
    Args:
        fileSize (int): The total log size after every 10 successfully read lines.
        statusCodes (dict): The dictionary of status codes and their counts.
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))

if __name__ == '__main__':
    parseLogs()

