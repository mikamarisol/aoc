import re

from patterns import *
from bigtree import Node


class DirectoryTree:

    def __init__(self, directory_navigation_file):
        with open(directory_navigation_file) as file:
            self.directory_navigation = file.read(20480).splitlines()[1:]
        self.tree = self.tree_from_instructions()

    def tree_from_instructions(self):

        root = Node('/')
        current_dir = root
        for instruction in self.directory_navigation:
            if GO_TO_PARENT_PATTERN.match(instruction):
                print(instruction, 'going up')
            elif GO_TO_NODE_PATTERN.match(instruction):
                name = GO_TO_NODE_PATTERN.match(instruction).group('name')
                # current_dir = current_dir.children
                print(instruction, 'making node', name)
            elif LIST_CHILDREN_PATTERN.match(instruction):
                print(instruction)
            elif LEAF_PATTERN.match(instruction):
                size = LEAF_PATTERN.match(instruction).group('size')
                name = LEAF_PATTERN.match(instruction).group('name')
                print(instruction, 'leaf size {} name {}'.format(size, name))
            elif DIRECTORY_PATTERN.match(instruction):
                name = DIRECTORY_PATTERN.match(instruction).group('name')
                print(instruction, name)
            # print(current_dir)


if __name__ == '__main__':
    terminal_output_file = '../../resources/directory_navigation_output.txt'
    tree = DirectoryTree(terminal_output_file)
    print(tree.tree_from_instructions())
