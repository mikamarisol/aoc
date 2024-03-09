import math
import operator


class Item:

    def __init__(self, worry_level):
        self.worry_level = worry_level

    def relax_worry(self):
        self.worry_level = math.floor(self.worry_level / 3)
        print(f'\tMonkey gets bored with item. Worry level is divided by 3 to {self.worry_level} ')


def set_operation(operation_string):
    ops = {'+': operator.add,
           '*': operator.mul}
    return ops[operation_string]


class Monkey:

    def __init__(self, name, items, operation_parameters, throwing_parameters):
        self.name = name
        self.items_holding = items

        self.worry_operation_string = operation_parameters[0]
        self.worry_operation = set_operation(operation_parameters[0])
        self.worry_parameter = operation_parameters[1]
        self.test_divisor, self.monkey_true_name, self.monkey_false_name = throwing_parameters
        self.items_inspected = []

    def inspect_item(self, item):
        print(f'\tMonkey inspects an item with a worry level of {item.worry_level}')
        item.worry_level = self.worry_operation(item.worry_level, self.worry_parameter)
        print(f'\tWorry level {self.worry_operation_string} by {self.worry_parameter} to {item.worry_level}.')
        if item not in self.items_inspected:
            self.items_inspected.append(item)
        print(f'\t\tMonkey has inspected {len(self.items_inspected)} distinct items')
        item.relax_worry()

    def throw_item(self, item):
        if item.worry_level % self.test_divisor == 0:
            print(f'\tCurrent worry level is divisible by {self.test_divisor}')
            monkey_to_throw_to = self.monkey_true_name
            # monkey_to_throw_to_if_true.items_holding.append(item)
        else:
            print(f'\tCurrent worry level is not divisible by {self.test_divisor}')
            monkey_to_throw_to = self.monkey_false_name
            # monkey_to_throw_to_if_false.items_holding.append(item)
        print(f'\tItem with worry level {item.worry_level} is thrown to monkey {monkey_to_throw_to}')

    def take_turn(self):
        print(f'Monkey {self.name}:')
        for item in self.items_holding:
            self.inspect_item(item)
            self.throw_item(item)
            print()

if __name__ == '__main__':
    item = Item(79)
    another = Item(98)
    items = [item, another]
    monkey = Monkey('george', items, ['*', 19], [23, 2, 3])
    monkey.take_turn()

    item = Item(54)
    another = Item(65)
    items = [item, another]
    monkey = Monkey('fred', items, ['+', 6], [19, 2, 0])
    monkey.take_turn()