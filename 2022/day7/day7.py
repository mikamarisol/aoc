from patterns import *
from directory import Directory
from file import File

instructions_file = '../resources/directory_navigation_output.txt'

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


def sum_small_files():
    instructions = read_instructions(instructions_file)
    directory = directory_from_instructions(instructions)

    size_limit = 100000
    sum_small_sizes = 0

    descendants = directory.get_descendants()
    while True:
        try:
            descendant = next(descendants)
            if descendant.size <= size_limit:
                sum_small_sizes += descendant.size
        except StopIteration:
            break

    return sum_small_sizes


def smallest_directory():
    instructions = read_instructions(instructions_file)
    directory = directory_from_instructions(instructions)

    disk_space = 70000000
    required_space = 30000000
    used_space = directory.size
    unused_space = disk_space - used_space
    space_needed = required_space - unused_space

    print('used {} out of {}, need {} more free'.format(used_space, disk_space, space_needed))

    smallest = used_space
    descendants = directory.get_descendants()
    while True:
        try:
            descendant = next(descendants)
            if space_needed <= descendant.size < smallest:
                smallest = descendant.size
        except StopIteration:
            break
    return smallest



if __name__ == '__main__':
    # print(sum_small_files())
    print(smallest_directory())
