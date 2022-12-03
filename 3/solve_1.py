import math


f = open('test_input')
input_lines = f.readlines()

def get_priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def find_dup(first, second):
    for i in first:
        if i in second:
            return i
    return None

total_priority = 0
for line in input_lines:
    half = math.floor(len(line) / 2)
    first = line[:half]
    second = line[half:]
    dup = find_dup(first, second)
    dup_priority = get_priority(dup)
    total_priority += dup_priority

print(f"Total priority: {total_priority}")