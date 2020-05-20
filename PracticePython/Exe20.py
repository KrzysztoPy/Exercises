from random import randint
import math

sorted_list = set()


def gen_list():
    for i in range(0, randint(0, 100)):
        list.add(randint(0, 100))
    sorted(sorted_list)


def normal_search(collection, value):
    if value in collection:
        return print("It is in collection")
    return print("It is not in collection")


# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8
# Extras:
def binary_search(collection=set(), value=0):
    while True:
        if len(collection) > 1:
            if collection[math.ceil((len(collection)) / 2) - 1] > value:
                for i in range(len(collection) - 1, (math.ceil((len(collection)) / 2)) - 2, -1):
                    collection.remove(collection[i])
            elif collection[math.ceil((len(collection)) / 2) - 1] < value:
                for i in range(0, (math.ceil((len(collection)) / 2)), 1):
                    collection.remove(collection[0])
            elif collection[math.ceil((len(collection)) / 2) - 1] == value:
                return print("It is in collection")
        else:
            if collection[0] == value:
                return print("It is in collection")
            else:
                return print("It is not in collection")


def test():
    test_list0 = [1, 2, 3, 4, 5, 6, 7, 8]
    test_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1, 10, 1):
        print("Whether {} is in list?".format(i))
        binary_search(test_list0.copy(), i)
        print("Whether {} is in list?".format(i))
        binary_search(test_list1.copy(), i)


test()
# gen_list()
# normal_search(sorted_list, 1)
# binary_search
# print(sorted_list)
