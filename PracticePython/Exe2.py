# while True:
#     try:
#         input_num = int(input("Give me a number: "))
#         break
#     except ValueError:
#         print("You must give a number. Try again.")
#
# if input_num % 2 == 0:
#     # Extras 1:
#     if input_num % 4 == 0:
#         print("Number is a multiple of 4.")
#     else:
#         print("Number is even")
# else:
#     print("Number is odd")

# Extras 2

while True:
    try:
        num = int(input("Give me a number: "))
        break
    except ValueError:
        print("You must give a number. Try again.")
while True:
    try:
        check = int(input("Give me a number: "))
        break
    except ValueError:
        print("You must give a number. Try again.")
if num % check == 0:
    print("The number is divided evenly.")
else:
    print("The number isn't divided evenly.")
