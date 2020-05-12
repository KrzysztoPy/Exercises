from random import randint

a = []

for i in range(0, randint(0, 30)):
    a.append(randint(0, 1000))
print("Whole list: {}".format(a))
print("First elem: {}\n Last elem: {}".format(a[0], a[a.__len__() - 1]))
