import re

GO_TO_PARENT_STRING = r'\$ cd \.{2}'
GO_TO_PARENT_PATTERN = re.compile(GO_TO_PARENT_STRING)

GO_TO_NODE_STRING = r'\$ cd (?P<name>.+)'
GO_TO_NODE_PATTERN = re.compile(GO_TO_NODE_STRING)

LIST_CHILDREN_STRING = r'\$ ls'
LIST_CHILDREN_PATTERN = re.compile(LIST_CHILDREN_STRING)

LEAF_STRING = r'(?P<size>[0-9]+) (?P<name>.+)'
LEAF_PATTERN = re.compile(LEAF_STRING)

DIRECTORY_STRING = r'dir (?P<name>.+)'
DIRECTORY_PATTERN = re.compile(DIRECTORY_STRING)