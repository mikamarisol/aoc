import numpy as np


def read_trail():
    with open('../resources/rope_trail.txt') as trail_file:
        instructions = trail_file.read().splitlines()
        trail_file.close()
        trail = []
    for instruction in instructions:
        instruction = instruction.split(' ')
        if instruction[0] == 'R':
            step = np.array([1, 0])
        elif instruction[0] == 'L':
            step = np.array([-1, 0])
        elif instruction[0] == 'U':
            step = np.array([0, 1])
        elif instruction[0] == 'D':
            step = np.array([0, -1])
        for n in range(int(instruction[1])):
            trail.append(step)
    return trail


def move_rope(trail):
    H = np.array([0, 0])
    T = np.array([0, 0])
    H_trail = [H]
    T_trail = [T]

    for h in trail:
        H = take_step(H, h)
        H_trail.append(H)
        if not are_touching(H, T):
            t = T_step(H, T)
            T = take_step(T, t)
        T_trail.append(T)

    return H_trail, T_trail


def take_step(position, d):
    return position + d


def are_touching(H, T):
    return max(abs(displacement(H, T))) == 1


def T_step(H, T):
    return np.sign(displacement(H, T))


def displacement(H, T):
    return H - T


if __name__ == '__main__':
    trail = read_trail()
    H_trail, T_trail = move_rope(trail)
    print(T_trail)
    print(len(np.unique(T_trail, axis=0)))

