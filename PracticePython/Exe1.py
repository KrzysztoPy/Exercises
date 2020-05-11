import datetime

name = input("Give me your name: ")
surname = input("Give me your surname: ")
while True:
    try:
        age = int(input('Your age on this year: '))
        break
    except ValueError:
        print("Enter the year using numbers. Try again! ")

print('{} will be 100 years old in the year {} \n'.format(name, int((datetime.datetime.now()).year) - age + 100))
number = input("Give me a number: ")
# Extras 1 :
print(number * int(number))
# Extras 2 :
print('{}\n'.format(number) * int(number))
