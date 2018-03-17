import csv
import sys

with open(sys.argv[1], newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    freq = [ 0 ] * 45
    next(csv_reader)        # remove header row
    rows = 0
    for row in csv_reader:
        draw, date_str, numbers = (row[0], row[1], row[2:8])
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
# Convert to list of tuples
lt = [(i+1, freq[i]) for i in range(len(freq))]
print(lt)
print('length = {}'.format(len(lt)))
# Sort list of tuples by frequency
slt = sorted(lt, key=lambda item: (item[1], item[0]), reverse=True)
print(slt)
print('length = {}'.format(len(slt)))
# First six tuples
firstsix = [slt[i] for i in range(6)]
# First six sorted by number
sortedhighest = sorted(firstsix, key=lambda item: (item[0], item[1]))
print(sortedhighest)

