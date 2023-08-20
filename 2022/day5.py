import re
import numpy as np
from collections import deque

instruction_pattern = r'move\s+(\d+)\s+from\s+(\d+)\s+to\s+(\d+)'
grid_pattern = r'(\[[A-Z]\]|\s\s\s)\s?'
labels_pattern = r'(\d)'


def read_message(stacks):
    message = ''
    for stack in stacks:
        message += stack[-1][1]
    return message


def sort_stacks():
    grid = read_crate_grid()
    instructions = read_crate_instructions()
    stacks = crate_grid_to_stacks(grid)

    for instruction in instructions:
        apply_instruction_crate_mover_9001(instruction, stacks)

    return stacks


def read_crate_grid():
    with open('resources/crate-stacks.txt') as crate_stacks_file:
        file_lines = crate_stacks_file.read(20480).splitlines()
        grid = []
        i = 0
        row = re.findall(grid_pattern, file_lines[i])
        labels = re.findall(labels_pattern, file_lines[i])
        while len(row) > 0 and not labels:
            grid.append(row)
            i += 1
            row = re.findall(grid_pattern, file_lines[i])
            labels = re.findall(labels_pattern, file_lines[i])

        columns = len(labels)
        for row in grid:
            row_length = len(row)
            if row_length != columns:
                row += ['   '] * (columns - row_length)

        return np.array(grid)


def read_crate_instructions():
    with open('resources/crate-stacks.txt') as crate_stacks_file:
        file_lines = crate_stacks_file.read(20480).splitlines()
        instructions = []

    i = 0
    while not re.match(instruction_pattern, file_lines[i]):
        i += 1
    instructions = [instruction_to_vector(line) for line in file_lines[i:]]
    return instructions


def apply_instruction_crate_mover_9000(vector_instruction, grid):
    amount = vector_instruction[0]
    source = vector_instruction[1] - 1
    destination = vector_instruction[2] - 1
    while amount > 0:
        moved_crate = grid[source].pop()
        grid[destination].append(moved_crate)
        amount -= 1
    return grid


def apply_instruction_crate_mover_9001(vector_instruction, grid):
    amount = vector_instruction[0]
    source = vector_instruction[1] - 1
    destination = vector_instruction[2] - 1
    moved = []
    while amount > 0:
        moved_crate = grid[source].pop()
        moved.append(moved_crate)
        amount -= 1
    moved.reverse()
    for crate in moved:
        grid[destination].append(crate)
    return grid


def crate_grid_to_stacks(grid):
    rotated_grid = np.rot90(grid, 3)
    return [deque([crate for crate in stack if crate != '   ']) for stack in rotated_grid]


def stacks_to_crate_grid(stacks):
    # TODO: for simulation
    pass

def instruction_to_vector(instruction):
    match = re.match(instruction_pattern, instruction)
    amount = int(match.group(1))
    source = int(match.group(2))
    destination = int(match.group(3))
    vector = np.array([amount, source, destination])
    return vector


if __name__ == '__main__':
    print(read_message(sort_stacks()))
