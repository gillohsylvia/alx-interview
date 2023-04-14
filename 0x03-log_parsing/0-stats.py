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

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
