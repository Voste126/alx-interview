#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_counts = {}
line_count = 0
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        # Validate format and parse parts of the line
        if len(parts) < 7:
            continue
        ip, dash, date, method, path, protocol, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]
        
        # Update total file size
        try:
            total_size += int(file_size)
        except ValueError:
            continue
        
        # Update status code count
        if status_code in status_codes:
            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1

        # Print metrics after every 10 lines
        if line_count % 10 == 0:
            print("File size:", total_size)
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    # Print metrics upon keyboard interruption
    print("\nFile size:", total_size)
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
    raise

# Final output if script ends naturally
finally:
    print("File size:", total_size)
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

