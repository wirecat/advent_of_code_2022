import math


f = open('input')
input_lines = f.readlines()

def is_superset(superset, subset):
    return subset[0] >= superset[0] and subset[1] <= superset[1]

def get_set(set_str):
    split_set = set_str.split('-')
    return [int(split_set[0]), int(split_set[1])]

total_supersets = 0
for line in input_lines:
    areas = line.split(',')
    elf1_area = get_set(areas[0])
    elf2_area = get_set(areas[1])

    if is_superset(elf1_area, elf2_area) or is_superset(elf2_area, elf1_area):
        total_supersets += 1

print(f'Total: {total_supersets}')