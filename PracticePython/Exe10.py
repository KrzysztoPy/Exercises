from random import randint

list_a = []
list_b = []


def rand_list():
    for i in range(0, 20):
        list_a.append(randint(0, 20))
        list_b.append(randint(0, 20))


def view_lists():
    print(list_a)
    print(list_b)


def contain_list():
    '''
    Combines the joint of two lists into one without repetition
    :return:
    '''
    print([i for i in set(list_a) if i in list_b])


def main():
    rand_list()
    view_lists()
    contain_list()


main()
