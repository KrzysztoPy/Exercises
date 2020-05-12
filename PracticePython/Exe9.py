from random import randint


def in_num():
    '''
    Draws number from 1 to 9. Then waiting for a data from the user and interprets it.
    You can stop program by typing "exit".
    Have shot counter.
    :return:
    '''
    drawn_num = randint(1, 10)
    shot_counter = 0

    while True:
        while True:
            try:
                input_num = input("Give me a number: ")
                # Extras 1
                if input_num == "exit":
                    exit()
                input_num = int(input_num)
                shot_counter += 1
                break
            except ValueError:
                print("You can only write a number. Try again.")
        if input_num < drawn_num:
            print("Too low")
        elif input_num > drawn_num:
            print("Too High")
        else:
            print("\nExactly right")
            print("Shot counter: {}".format(shot_counter))
            break


def menu():
    in_num()


menu()
