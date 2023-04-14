#!/usr/bin/python3

import sys

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

status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 405: 0, 500: 0}
stdin = sys.stdin
counter = 0
total_file_size = 0

try:
    for line in stdin:
        output = line.split()
        if int(output[-2]) in status_dict.keys() and len(output) == 9:
            counter += 1
            status_dict[int(output[-2])] += 1
            total_file_size += int(output[-1])
        if counter % 10 == 0:
            print('File size: {}'.format(total_file_size))
            for key, value in status_dict.items():
                if value:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt:
    print('File size: {}'.format(total_file_size))
    for key, value in status_dict.items():
        if value:
            print("{}: {}".format(key, value))
    raise
