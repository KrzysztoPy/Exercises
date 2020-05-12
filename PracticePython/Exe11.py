dividers = []


def get_int():
    while True:
        try:
            return int(input("Give me a number: "))
        except ValueError:
            print("Wrong input data. Try again.")


def all_dividers():
    '''
    Creates list with all dividers without 1.
    :return:
    '''
    for i in range(2, get_int() + 1):
        dividers.append(i)


def num_is_prime():
    '''
    Check whether number is prime.
    :return:
    '''
    if [i for i in dividers if (((dividers.__len__() + 1) % i) == 0)]:
        print("Number is a prime number.")
    else:
        print("Number isn't prime number.")


def menu():
    all_dividers()
    num_is_prime()


menu()
