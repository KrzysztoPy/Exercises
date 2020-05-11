a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i != 5:
        print(i)
# # Extras 1
b = []
for i in a:
    if i < 5:
        b.append(i)
print(b)
# Extras 2
print([i for i in a if i < 5])
# Extras 3
while True:
    try:
        in_num = int(input("Give me a number"))
        break
    except ValueError:
        print("Wrong input data. Try again!")
print([i for i in a if i < in_num])
