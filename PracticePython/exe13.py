# fibb 0 1 1 2 3 5 8 13

def max_range():
    while True:
        try:
            return int(input("Give me a number: "))
        except ValueError:
            print("Wrong input data. Try again.")


def fibb(num=max_range()):
    first_num = 0
    second_num = 1
    print(first_num)
    print(second_num)
    while True:
        tmp = second_num
        second_num = first_num + second_num
        if (second_num > num):
            break
        first_num = tmp
        print(second_num)


def menu():
    fibb()


menu()
