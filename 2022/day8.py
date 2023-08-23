import numpy as np


def read_forest_map():
    with open('../resources/forest.txt') as forest_grid_file:
        forest = forest_grid_file.read().splitlines()
        forest_grid_file.close()

    m = len(forest)
    n = len(forest[0])
    # forest[j][i] = x_i, y_j
    heights = np.array([[int(forest[j][i]) for i in range(n)] for j in range(m)])
    # already know edges are visible
    visibles = np.array([[1 if i in (0, n - 1) or j in (0, m - 1) else 0 for i in range(n)] for j in range(m)])
    forest_map = np.stack([heights, visibles])
    return forest_map, n, m


def how_many_visible(map, n, m):
    for i in range(1, n-1):
        for j in range(1, m-1):
            for direction in ['N', 'E', 'S', 'W']:
                if is_visible(map, i, j, direction):
                    map = set_visible(map, i, j)
                    break
    print(map[1])
    return np.count_nonzero(map[1] == 1)


def is_visible(map, i, j, direction):
    if direction == 'N':
        if (map[0, j, i] > map[0, :j, i]).all():
            return True
    if direction == 'E':
        if (map[0, j, i] > map[0, j, i+1:]).all():
            return True
    elif direction == 'S':
        if (map[0, j, i] > map[0, j+1:, i]).all():
            return True
    elif direction == 'W':
        if (map[0, j, i] > map[0, j, :i]).all():
            return True


def set_visible(map, i, j):
    map[1, j, i] = 1
    return map


if __name__ == '__main__':
    # forest[k][j][i] = x_i, y_j, z_k
    # k = 0 -> heights
    # k = 1 -> visibles
    map, n, m = read_forest_map()
    print(map[0])
    print(how_many_visible(map, n, m))
