import numpy as np


def read_location_id_lists():
    with open('resources/location_id_lists.txt') as id_lists:
        list1, list2 = np.loadtxt('resources/location_id_lists.txt', unpack=True, dtype=int)
        return list1, list2


def total_list_distance(list1, list2):
    list1.sort()
    list2.sort()
    return sum([abs(list1[i] - list2[i]) for i in range(len(list1))])


def similarity_score(list1, list2):
    return sum([list1[i] * list(list2).count(list1[i]) for i in range(len(list1))])


if __name__ == '__main__':
    list1, list2 = read_location_id_lists()
    print(total_list_distance(list1, list2))
    print(similarity_score(list1, list2))
