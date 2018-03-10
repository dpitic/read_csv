import csv
import sys

with open(sys.argv[1], newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    freq = [ 0 ] * 40
    next(csv_reader)        # remove header row
    rows = 0
    for row in csv_reader:
        draw, date_str, numbers = (row[0], row[1], row[2:8])
        if int(draw) < 878:     # different rules before this time
            break
        rows += 1
        for i in numbers:
            freq[int(i)-1] += 1
print(freq)
print('length = {}'.format(len(freq)))
print('rows = {}'.format(rows))
maximum = max(freq)
n_max = freq.index(maximum) + 1
print('max = {}; number = {}'.format(maximum, n_max))
minimum = min(freq)
n_min = freq.index(minimum) + 1
print('min = {}; number = {}'.format(minimum, n_min))
