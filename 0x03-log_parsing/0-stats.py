#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys

# Initialize storage for status codes and total file size
cache = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split()
        if len(line_list) > 4:
            code = line_list[-2]
            try:
                size = int(line_list[-1])
                total_size += size
            except ValueError:
                continue  # Ignore lines with invalid file sizes

            if code in cache:
                cache[code] += 1
            counter += 1

        if counter == 10:
            print('File size: {}'.format(total_size))
            for key in sorted(cache.keys()):
                if cache[key] != 0:
                    print('{}: {}'.format(key, cache[key]))
            counter = 0

except (KeyboardInterrupt, SystemExit):
    pass
finally:
    print('File size: {}'.format(total_size))
    for key in sorted(cache.keys()):
        if cache[key] != 0:
            print('{}: {}'.format(key, cache[key]))

