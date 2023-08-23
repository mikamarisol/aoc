from patterns import *
from directory import Directory
from file import File


def read_instructions(directory_navigation_file):
    with open(directory_navigation_file) as file:
        return file.read(20480).splitlines()[1:]


def directory_from_instructions(directory_navigation):
    root = Directory('/')
    current_dir = root
    for instruction in directory_navigation:

        if GO_TO_PARENT_PATTERN.match(instruction):
            current_dir = current_dir.parent

        elif GO_TO_DIR_PATTERN.match(instruction):
            name = GO_TO_DIR_PATTERN.match(instruction).group('name')
            current_dir = current_dir.get_directory(name)

        elif FILE_PATTERN.match(instruction):
            size = int(FILE_PATTERN.match(instruction).group('size'))
            name = FILE_PATTERN.match(instruction).group('name')
            current_dir.create_file(File(name, size))

        elif DIR_PATTERN.match(instruction):
            name = DIR_PATTERN.match(instruction).group('name')
            current_dir.create_directory(Directory(name))

        current_dir.update_size()

    root.update_size()
    return root

if __name__ == '__main__':
    instructions_file = '../../resources/directory_navigation_output.txt'
    instructions = read_instructions(instructions_file)
    directory = directory_from_instructions(instructions)
    size_limit = 100000

    print(directory.size)
    print(directory)

    descendants = directory.get_descendants()
    sum_sizes_under_limit = sum([child.size for child in descendants if child.size <= size_limit ])
    print(sum_sizes_under_limit)

