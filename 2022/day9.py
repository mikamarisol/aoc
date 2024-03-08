import numpy as np

from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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


def animate(i):
    pt = randint(1,9) # grab a random integer to be the next y-value in the animation
    hx.append(H_trail[i][0])
    hy.append(H_trail[i][1])

    tx.append(T_trail[i][0])
    ty.append(T_trail[i][1])

    ax.clear()
    ax.plot(hx, hy, marker='$H$')
    ax.plot(tx, ty, marker='$T$')
    ax.grid()
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])


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


def move_long_rope(trail):
    H = np.array([0, 0])
    knots = [H] + [np.array([0, 0]) for knot in range(9)]
    T_trail = [knots[-1]]

    for h in trail:
        H = take_step(H, h)
        knots[0] = H
        for k in range(1, len(knots)):
            if not are_touching(knots[k-1], knots[k]):
                t = T_step(knots[k-1], knots[k])
                knots[k] = take_step(knots[k], t)
            T_trail.append(knots[-1])
    return T_trail

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
    # T_trail = (move_long_rope(trail))
    # print(len(np.unique(T_trail, axis=0)))
    hx=[]
    hy=[]
    tx=[]
    ty=[]
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate, frames=2000, interval=200, repeat=False)
    plt.show()