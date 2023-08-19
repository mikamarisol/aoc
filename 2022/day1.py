import itertools


def read_calories_list():
    with open('resources/calories.txt') as calories:
        return [line_to_int(line) for line in calories.readlines()]


def line_to_int(line):
    return None if line == '\n' else int(line.strip())


def calories_grouped_by_elf():
    calories = read_calories_list()
    return [list(group) for key, group in itertools.groupby(calories, lambda x: x is None) if not key]


def calories_summed_by_elf():
    grouped_calories = calories_grouped_by_elf()
    return [sum(calories) for calories in grouped_calories]


def most_food():
    return max(calories_summed_by_elf())


def top_x_most_food(x):
    return sum(sorted(calories_summed_by_elf(), reverse=True)[0:x])


if __name__ == '__main__':
    print(top_x_most_food(3))
