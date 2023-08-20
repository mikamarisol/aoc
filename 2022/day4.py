def read_pair_assignments():
    with open('resources/paired_sections.txt') as assignments:
        pair_assignments = []
        for line in assignments.readlines():
            data = line.strip().split(',')
            a = [int(limit) for limit in data[0].split('-')]
            b = [int(limit) for limit in data[1].split('-')]
            pair_assignments.append([a, b])
        return pair_assignments


def how_many_overlaps():
    pair_assignments = read_pair_assignments()
    return len([pair for pair in pair_assignments if is_overlapping(pair, total_overlap=False)])


def is_overlapping(pair, total_overlap=True):
    a_set = set(range(pair[0][0], pair[0][1] + 1))
    b_set = set(range(pair[1][0], pair[1][1] + 1))
    intersection = a_set.intersection(b_set)
    if total_overlap:
        return intersection == a_set or intersection == b_set
    return intersection != set()


if __name__ == '__main__':
    print(how_many_overlaps())
