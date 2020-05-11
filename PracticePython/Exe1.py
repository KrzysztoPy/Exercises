import datetime

name = input("Give me your name: ")
surname = input("Give me your surname: ")
age = int(input('Yor age on this year: '))
print('{} will be 100 years old in the year {} \n'.format(name, int((datetime.datetime.now()).year) - age + 100))
