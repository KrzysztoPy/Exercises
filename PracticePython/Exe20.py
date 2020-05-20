from random import randint

list = set()


def gen_list():
    for i in range(0, randint(0, 100)):
        list.add(randint(0, 100))
    sorted(list)


def normal_search(collection, value):
    if value in collection:
        return print("It is in collection")
    return print("It is not in collection")


gen_list()
normal_search(list, 1)
print(list)
