import re

from patterns import *
from directory import Directory


def read_instructions(directory_navigation_file):
    with open(directory_navigation_file) as file:
        return file.read(20480).splitlines()[1:]


def tree_from_instructions(directory_navigation):
    root = Directory('/')
    current_dir = root
    for instruction in directory_navigation:

        if GO_TO_PARENT_PATTERN.match(instruction):
            current_dir = current_dir.parent
            # print(instruction, 'going up')

        elif GO_TO_DIR_PATTERN.match(instruction):
            name = GO_TO_DIR_PATTERN.match(instruction).group('name')
            # current_dir = current_dir.children
            # print(instruction, 'going to node', name)

        elif LIST_CHILDREN_PATTERN.match(instruction):
            # print(instruction)

        elif FILE_PATTERN.match(instruction):
            size = FILE_PATTERN.match(instruction).group('size')
            name = FILE_PATTERN.match(instruction).group('name')
            # print(instruction, 'leaf size {} name {}'.format(size, name))

        elif DIR_PATTERN.match(instruction):
            name = DIR_PATTERN.match(instruction).group('name')
            # print(instruction, name)
        # print(current_dir)


if __name__ == '__main__':
    instructions_file = '../../resources/directory_navigation_output.txt'
    instructions = read_instructions(instructions_file)
    print(tree_from_instructions(instructions))
