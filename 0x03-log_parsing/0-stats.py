#!/usr/bin/python3

import sys
from collections import OrderedDict

"""
My pseudocode
* read from the stdin for line in stdin.
* check if format is stdin, else skip.
* Declare a counter variable that increments.
* check if the counter is 10.
* Declare a dictionary for storing the status codes.
* Declare a variable to store the file size.
* Check if key is available in dict every time a line is read. 
* update file size
* print file size
* if !key || !value, continue else print status code
"""

def parseLogs():


    """
    Reads logs from standard input and generates reports
    Reports:
        * Prints log size after reading every 10 lines 
        & at KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles this exception and raises it
    """
count = 0
    global file_size
    global status_dict
    file_size = 0
    status_dict = {200: 0,
                   301: 0,
                   400: 0,
                   401: 0,
                   403: 0,
                   404: 0,
                   405: 0,
                   500: 0}

    for line in sys.stdin:
        logs = line.split(" ")
        if int(logs[-2]) in status_dict.keys() and len(logs) == 9:
            file_size += int(logs[-1])
            status_dict[int(logs[-2])] += 1
        if count % 10 == 0 and count != 0:
            print_output(status_dict, file_size)
        count += 1


def print_output(status_dict, file_size):
    """
    Prints generated report to standard output
    Args:
        fileSize (int): This is the total log size after
        every 10 successfully read line
        statusCodes (dict): The dictionary of status codes and counts
    """
    print("File size: {}".format(file_size))
    for k, v in status_dict.items():
        if v > 0:
            print("{}: {}".format(k, v))


try:
    parse_logs()
except KeyboardInterrupt:
    print_output(status_dict, file_size)
