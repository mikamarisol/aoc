import re


def read_cathode_ray_instructions():
    with open('resources/cathode_ray_instructions.txt') as instructions_file:
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
            # print(c + 1, apply_cpu_cycle_instructions(cycle_instructions, c))
            signal_strength += apply_cpu_cycle_instructions(cycle_instructions, c)[2]
    return signal_strength


def apply_crt_cycle_instructions(cycle_instructions):
    crt_output = ''
    for c in range(len(cycle_instructions)):
        # print(c + 1, draw_sprite(apply_cpu_cycle_instructions(cycle_instructions, c)[1]))
        cycle, x, signal_strength = apply_cpu_cycle_instructions(cycle_instructions, c)
        sprite = draw_sprite(x)
        if sprite[c % 40] == '#':
            crt_output += '#'
        else:
            crt_output += '.'
        # print('crt', crt_output)
    return crt_output


def draw_crt_output(crt_output):
    return '\n'.join(crt_output[i : i + 40] for i in range(0, len(crt_output), 40))


def draw_sprite(x):
    sprite = ['#' if x-1 <= i <= x+1 else '.' for i in range(40)]
    return sprite

if __name__ == '__main__':
    cycle_instructions = read_cathode_ray_instructions()
    # print(sum_signal_strengths_at_intervals(cycle_instructions, 20, 40))
    crt_output = apply_crt_cycle_instructions(cycle_instructions)
    print(draw_crt_output(crt_output))
