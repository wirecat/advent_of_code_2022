import math


f = open('input')
input_lines = f.readlines()

def overlaps(first_set, second_set):
    return (first_set[0] <= second_set[1] and first_set[0] >= second_set[0]) or \
        (first_set[1] >= second_set[0] and first_set[1] <= second_set[1])

def get_set(set_str):
    split_set = set_str.split('-')
    return [int(split_set[0]), int(split_set[1])]

total_overlaps = 0
for line in input_lines:
    areas = line.split(',')
    elf1_area = get_set(areas[0])
    elf2_area = get_set(areas[1])

    if overlaps(elf1_area, elf2_area) or overlaps(elf2_area, elf1_area):
        total_overlaps += 1

print(f'Total: {total_overlaps}')