from random import randint


def gen_num():
    return randint(1000, 10000)


range_num = [3, 5]
gen_number = str(gen_num())


def get_num():
    while True:
        try:
            tmp = input("Enter a number: ")
            if tmp == "show me the number":
                print("Hi cheater :P. Your number: {}".format(gen_number))
                continue
            int(tmp)
            if str(tmp).__len__() <= range_num[0]:
                print("Number is too short. Number must have {} number.".format(range_num[0] + 1))
                continue
            elif str(tmp).__len__() >= range_num[1]:
                print("Number is too long. Number must have {} number.".format(range_num[0] + 1))
                continue
            return str(tmp)
        except ValueError:
            print("You only write number. Please try again!!")


def cows_bulls_logic():
    cows_last_shot = [0, 0, 0, 0]
    move_count = 0
    cows = 0
    bulls = 0

    # print(gen_number)
    print("Welcome to the Cows and Bulls Game!")
    while True:
        input_num = get_num()
        move_count += 1
        for i in range(0, range_num[0] + 1):
            if gen_number[i] == input_num[i]:
                if cows_last_shot[i] != 1:
                    cows_last_shot[i] = 1
                    cows += 1
            elif gen_number[i] != input_num[i]:
                if cows_last_shot[i] == 1:
                    cows_last_shot[i] = 0
                    cows -= 1
                    bulls += 1
        if cows == 4:
            print(
                "Congratulation you are winner! \n Move counter: {} \n Generation number: {} \n Your number: {}".format(
                    move_count, gen_number,
                    input_num))
            break

        print("Cows: {}, bulls: {}".format(cows, bulls))
        bulls = 0


def test_get_num():
    cows_bulls_logic()
    # tmp = get_num()


test_get_num()
