player_1 = []
player_2 = []


def set_name(player_1, player_2):
    '''
    Set player name and check whether second player have another name from first player.
    :param player_1: First player: List: [0] -> Player name, [1] -> Game choice.
    :param player_2: Second player: List: [0] -> Player name, [1] -> Game choice.
    :return:
    '''
    name = input("Name player 1: ")
    player_1.append(name)
    while True:
        name = input("Name player 2: ")
        if name == player_1[0]:
            print("You must choice another name: ")
        else:
            player_2.append(name)
            break


def choice_symbol(name_player):
    '''
    Set what individual player choice and saves the player's list in second place.
    :param name_player: Any player: List: [0] -> Player name, [1] -> Game choice.
    :return:
    '''
    while True:
        try:
            choice = input(
                "{} choice: Rock press R or r, Paper press P or p, Scissors press S or s: ".format(name_player[0]))
            if choice != "R" and choice != "r" and choice != "P" and choice != "p" and choice != "S" and choice != "s":

                raise Exception("Wrong choice you can press only:Rock: (R/r),Paper (P/p) or Scissors (S/s)")
            else:
                name_player.append(choice)
                break

        except Exception as e:
            print(e)


def who_win(player_1, player_2):
    '''
    Compare choice and emerges from the winner
    :param player_1: First player: List: [0] -> Player name, [1] -> Game choice.
    :param player_2: Second player: List: [0] -> Player name, [1] -> Game choice.
    '''
    # player 1 '\33[91m'
    # player 2 '\33[96m'
    if player_1[1] == "R" or player_1[1] == "r":
        if player_2[1] == "S" or player_2[1] == "s":
            print('\33[91m', "Rock {} win! Congratulation.\n".format(player_1[0]))
        elif player_2[1] == "P" or player_2[1] == "p":
            print('\33[96m', "{} win! Congratulation.\n".format(player_2[0]))
        else:
            print('\33[94m', "DRAW!!!\n")
    elif player_1[1] == "P" or player_1[1] == "p":
        if player_2[1] == "S" or player_2[1] == "s":
            print('\33[96m', "{} win! Congratulation.\n".format(player_2[0]))
        elif player_2[1] == "R" or player_2[1] == "r":
            print('\33[91m', "{} win! Congratulation.\n".format(player_1[0]))
        else:
            print('\33[94m', "DRAW!!!\n")
    elif player_1[1] == "S" or player_1[1] == "s":
        if player_2[1] == "R" or player_2[1] == "r":
            print('\33[96m', "{} win! Congratulation.\n".format(player_2[0]))
        elif player_2[1] == "P" or player_2[1] == "p":
            print('\33[91m', "{} win! Congratulation.\n".format(player_1[0]))
        else:
            print('\33[94m', "DRAW!!!\n")


def test_who_win():
    '''
    Test check whether def who_win work correctly.
    '''
    player_x = ["Player_1", 0]
    player_y = ["Player_2", 0]
    choice = ["R", "P", "S"]
    flag = [0, 1]
    for i in range(0, 2):
        print('\33[93m', "Test number: {}\n".format(flag[i] + 1))
        for j in range(0, 3):
            for k in range(0, 3):
                if flag[i]:
                    player_x[1] = choice[j]
                    player_y[1] = choice[k]
                    print('\33[32m', "-" * 50)
                    print('\33[91m', "{} choice: {}\n".format(player_x[0], player_x[1]))
                    print('\33[96m', "{} choice: {}\n ".format(player_y[0], player_y[1]))
                    print('\33[32m', "-" * 50)
                    who_win(player_x, player_y)
                else:
                    player_x[1] = choice[k]
                    player_y[1] = choice[j]
                    print('\33[32m', "-" * 50)
                    print('\33[91m', "{} choice: {}\n".format(player_x[0], player_x[1]))
                    print('\33[96m', "{} choice: {}\n ".format(player_y[0], player_y[1]))
                    print('\33[32m', "-" * 50)
                    who_win(player_x, player_y)


# test_who_win()
set_name(player_1, player_2)
choice_symbol(player_1)
choice_symbol(player_2)
who_win(player_1, player_2)
