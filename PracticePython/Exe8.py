player_1 = []
player_2 = []
name = input("Name player 1: ")
player_1.append(name)
while True:
    name = input("Name player 2: ")
    if (name == player_1[0]):
        print("You must choice another name: ")
    else:
        break

while True:
    try:
        choice = input("{} choice: Rock press R or r, Paper press P or p, Scissors press S or s: ".format(player_1[0]))
        print(type(choice))
        print(choice.__len__())
        if ((choice != "R" and "r") and (choice != "P" and "p") and (choice != "S" and "s")):
            print("True")
        # if str(choice) == "R" and "r":
        #     print("Jest R")
        # elif str(choice) == "P" and "p":
        #     print("Jest P")
        # elif str(choice) == "S" and "s":
        #     print("Jest S")

        else:
            print("False")
            # raise Exception("Wrong choice you can press only:Rock: (R/r),Paper (P/p) or Scissors (S/s)")


    except Exception as e:
        print(e)
