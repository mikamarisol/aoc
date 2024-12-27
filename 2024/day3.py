import re

def read_memory():
    with open('resources/corrupted_memory.txt') as memory_file:
        memory = memory_file.read()
        return memory


def sum_instructions(memory):
    instructions = find_instructions(memory)
    sum = 0
    for instruction in instructions:
        x = int(instruction[0])
        y = int(instruction[1])
        sum += x * y
    return sum

def find_instructions(memory):
    multiply_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    return re.findall(multiply_pattern, memory)


if __name__ == '__main__':
    memory = read_memory()

    print(sum_instructions(memory))