import math


f = open('input')
input_lines = f.readlines()

def get_priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def find_dup(first, second, third):
    for i in first:
        if i in second and i in third:
            return i
    return None

def chunk(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

total_priority = 0
for group in chunk(input_lines, 3):
    dup = find_dup(group[0], group[1], group[2])
    dup_priority = get_priority(dup)
    total_priority += dup_priority

print(f"Total priority: {total_priority}")