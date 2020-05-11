while True:
    try:
        input_num = int(input("Give me a number: "))
        break
    except ValueError:
        print("You must give a number. Try again.")

if input_num % 2 == 0:
    # Extras 1:
    if input_num % 4 == 0:
        print("Number is a multiple of 4.")
    else:
        print("Number is even")
else:
    print("Number is odd")



