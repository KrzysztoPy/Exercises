from random import randint


class Exe14():
    a = []
    b = []

    def set_lists(self):
        for i in range(0, randint(0, 20)):
            self.a.append(randint(0, 20))
        for i in range(0, randint(0, 20)):
            self.b.append(randint(0, 20))

    def set_list(self):
        print(self.a)
        print(self.b)
        s = set(i for i in self.a if i in self.b)

        for i in s:
            print(i)


def menu():
    exe = Exe14()
    exe.set_lists()
    exe.set_list()


menu()
