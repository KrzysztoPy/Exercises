import string
import random


def pass_gen():
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(characters) for x in range(random.randint(1, 16)))
    print(password)


pass_gen()
