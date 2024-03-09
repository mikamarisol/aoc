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


def apply_cpu_cycle_instructions(cycle_instructions, cycle):
    x = 1 + sum(cycle_instructions[:cycle])
    return cycle + 1, x, (cycle + 1) * x


def sum_signal_strengths_at_intervals(cycle_instructions, start, interval):
    signal_strength = 0
    for c in range(len(cycle_instructions) + 1):
        if c + 1 == start or (c + 1) % interval == start:
            print(c + 1, apply_cpu_cycle_instructions(cycle_instructions, c))
            signal_strength += apply_cpu_cycle_instructions(cycle_instructions, c)[2]
    return signal_strength


def apply_crt_cycle_instructions(cycle_instructions):
    crt_output = []
    for c in range(len(cycle_instructions) + 1):
        print(c+1, draw_sprite(apply_cpu_cycle_instructions(cycle_instructions, c)[1]))
        cycle, x, signal_strength = apply_cpu_cycle_instructions(cycle_instructions, c)
        sprite = draw_sprite(x)
        print('checking sprite', sprite[cycle - 1:cycle + 2])
        if '#' in sprite[cycle - 1:cycle+ 2]:
            crt_output.append('#')
        else:
            crt_output.append('.')
        print('crt', crt_output)
    return crt_output


def draw_sprite(x):
    sprite = ['#' if x-1 <= i <= x+1 else '.' for i in range(40)]
    return sprite

if __name__ == '__main__':
    cycle_instructions = read_cathode_ray_instructions()
    # print(cycle_instructions)
    # print('cycle, x, strength')
    # print(sum_signal_strengths_at_intervals(cycle_instructions, 20, 40))
    print(apply_crt_cycle_instructions(cycle_instructions))
