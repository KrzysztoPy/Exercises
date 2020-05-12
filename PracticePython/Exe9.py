from random import randint


def in_num():
    '''
    Draws number from 1 to 9. Then waiting for a data from the user and interprets it.
    :return:
    '''
    drawn_num = randint(1, 10)

    while True:
        while True:
            try:
                input_num = int(input("Give me a number: "))
                break
            except ValueError:
                print("You can only write a number. Try again.")
        if input_num < drawn_num:
            print("Too low")
        elif input_num > drawn_num:
            print("Too High")
        else:

            print("Exactly right")
            break


def menu():
    in_num()


menu()
