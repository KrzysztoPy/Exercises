while True:
    try:
        in_num = int(input("Give me a number: "))
        break
    except ValueError:
        print("Wrong input data. Please try again!")
list_all_num = range(1, in_num + 1)
print([i for i in list_all_num if in_num % i == 0])
