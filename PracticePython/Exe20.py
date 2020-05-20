from random import randint
import math


def get_num():
    while True:
        try:
            num = int(input("Give me a number from 0 to 100: "))
            if num < 0:
                print("Number must be greater than 0 ")
                continue
            elif num > 100:
                print("Number must be less than 100 ")
                continue
            return num
        except ValueError:
            print("You can only enter a number from range 0 to 100 ")


def gen_list():
    sorted_list = set()
    for i in range(0, randint(1, 100)):
        sorted_list.add(randint(0, 100))
    print(sorted(sorted_list))
    return list(sorted(sorted_list.copy()))


def normal_search(collection, value):
    if value in collection:
        return print("It is in collection")
    return print("It is not in collection")


# Extras:
def binary_search(collection=[], value=0):
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
                print(collection)
                return print("It is in collection")
            else:
                print(collection)
                return print("It is not in collection")


# def test():
#     test_list0 = [1, 2, 3, 4, 5, 6, 7, 8]
#     test_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for i in range(1, 10, 1):
#         print("Whether {} is in list?".format(i))
#         binary_search(test_list0.copy(), i)
#         print("Whether {} is in list?".format(i))
#         binary_search(test_list1.copy(), i)


# test()
list_gen = gen_list()
normal_search(list_gen, get_num())
binary_search(list_gen, get_num())
# print(sorted_list)
