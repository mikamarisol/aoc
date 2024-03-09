import re


def read_cathode_ray_instructions():
    with open('../resources/cathode_ray_instructions.txt') as instructions_file:
        instructions = instructions_file.read().splitlines()
        instructions_file.close()
    addx_pattern = re.compile(r'addx (?P<value>-?\d+)')
    cycle_instructions = []
    for instruction in instructions:
        match = addx_pattern.match(instruction)
        cycle_instructions.append(0)
        if match:
            cycle_instructions.append(int(match.group('value')))
    return cycle_instructions


def get_strength_at_cycle(cycle_instructions, cycle):
    x = 1 + sum(cycle_instructions[:cycle])
    return cycle+1, x, (cycle+1) * x


def sum_signal_strengths_at_intervals(cycle_instructions, start, interval):
    signal_strength = 0
    for c in range(len(cycle_instructions)+1):
        if c + 1 == start or (c + 1) % interval == start:
            print(c+1, get_strength_at_cycle(cycle_instructions, c))
            signal_strength += get_strength_at_cycle(cycle_instructions, c)[2]
    return signal_strength


if __name__ == '__main__':
    cycle_instructions = read_cathode_ray_instructions()
    print(cycle_instructions)
    print('cycle, x, strength')
    print(sum_signal_strengths_at_intervals(cycle_instructions, 20, 40))
