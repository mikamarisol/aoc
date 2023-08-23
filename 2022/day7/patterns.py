import re

GO_TO_PARENT_STRING = r'\$ cd \.{2}'
GO_TO_PARENT_PATTERN = re.compile(GO_TO_PARENT_STRING)

GO_TO_DIR_STRING = r'\$ cd (?P<name>.+)'
GO_TO_DIR_PATTERN = re.compile(GO_TO_DIR_STRING)

LIST_CHILDREN_STRING = r'\$ ls'
LIST_CHILDREN_PATTERN = re.compile(LIST_CHILDREN_STRING)

FILE_STRING = r'(?P<size>[0-9]+) (?P<name>.+)'
FILE_PATTERN = re.compile(FILE_STRING)

DIR_STRING = r'dir (?P<name>.+)'
DIR_PATTERN = re.compile(DIR_STRING)