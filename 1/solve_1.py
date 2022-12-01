f = open('input')
input_lines = f.readlines()

total = 0
largest = 0
for line in input_lines:
    if len(line.strip('\n')) > 0:
        total = total + int(line)
    else:
        largest = total if total > largest else largest
        total = 0

print(largest)