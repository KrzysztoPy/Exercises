b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if a.__len__() > b.__len__():
    print([i for i in a if i in b])
else:
    print([i for i in b if i in a])
