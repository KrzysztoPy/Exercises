from random import randint

b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def common():
    print("List a: {} \nList b: {}\n".format(a, b))

    if a.__len__() > b.__len__():
        print("Common between a and b: {}".format([i for i in a if i in b]), "\n")
    elif a.__len__() < b.__len__():
        print("Common between a and b: {}".format([i for i in b if i in a]), "\n")
    elif a.__len__() == b.__len__():
        print("Common between a and b: {}".format([i for i in a if i in b]), "\n")


common()

# Extras 1
for i in range(0, randint(0, 15)):
    a.append(randint(0, 101))
for i in range(0, randint(0, 15)):
    b.append(randint(0, 101))
common()
