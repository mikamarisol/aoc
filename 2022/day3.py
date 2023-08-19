def open_rucksacks_by_compartment():
    with open('resources/rucksacks.txt') as rucksacks:
        return [separate_compartments(rucksack) for rucksack in rucksacks.readlines()]


def open_rucksacks_by_groups():
    with open('resources/rucksacks.txt') as rucksacks:
        group_size = 3
        rucksacks = [rucksack.strip() for rucksack in rucksacks.readlines()]
        return [rucksacks[i:i + group_size] for i in range(0, len(rucksacks), group_size)]


def separate_compartments(rucksack):
    rucksack = rucksack.strip()
    mid = int(len(rucksack) / 2)
    return [rucksack[:mid], rucksack[mid:]]


def find_common_items():
    rucksacks = open_rucksacks_by_compartment()
    common_items = [list(set(rucksack[0]).intersection(set(rucksack[1]))) for rucksack in rucksacks]
    return common_items


def find_badges():
    groups = open_rucksacks_by_groups()
    badges = [list(set(group[0]).intersection(set(group[1]), set(group[2]))) for group in groups]
    return badges


def sum_priorities():
    items = find_badges()
    return sum([char_to_priority(item[0]) for item in items])


def char_to_priority(char):
    if 96 < ord(char) <= 122:
        return ord(char) - 96
    elif 64 < ord(char) <= 90:
        return ord(char) - 64 + 26
    else:
        raise Exception


if __name__ == '__main__':
    print(sum_priorities())
