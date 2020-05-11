while True:
    try:
        input_num = int(input("Give me a number: "))
        break
    except ValueError:
        print("You must give a number. Try again.")

if input_num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
