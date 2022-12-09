import re

f = open('input')
input_lines = f.readlines()
input_lines = [line.strip('\n') for line in input_lines]

drawing_stop_row = input_lines.index('')
column_ids_row = drawing_stop_row -1

# Parse out the column ids, which will also tell us how many columns there are
column_ids = [int(x) for x in input_lines[drawing_stop_row - 1].split()]

# Parse out the stacks of crates
crate_stacks = [[] for x in column_ids]
for drawing_row in input_lines[:column_ids_row]:
    for column_id in column_ids:
        column_index = column_id - 1
        crate_label = drawing_row[1 + (4 * column_index)]

        if crate_label != ' ':
            crate_stacks[column_index].insert(0, crate_label)

# Class to represent a command
class command:
    def __init__(self, count, source, destination):
        self.count = count
        self.source = source
        self.destination = destination
    
    def __str__(self) -> str:
        return f'move {self.count} from {self.source} to {self.destination}'

    def __repr__(self) -> str:
        return self.__str__()

# Regex and helper function to parse commands
regex = re.compile("move (\d+) from (\d+) to (\d+)")
def get_command(command_string):
    match = regex.match(command_string)
    if match:
        return command(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    else:
        raise Exception("Invalid command: " + command_string)

# Parse the commands now
commands = [get_command(x) for x in input_lines[drawing_stop_row + 1:]]

# Perform the commands
for cmd in commands:
    for _ in range(cmd.count):
        crate_stacks[cmd.destination - 1].append(crate_stacks[cmd.source - 1].pop())

# Print top of each stack
for stack in crate_stacks:
    print(stack[-1], end='')
print()