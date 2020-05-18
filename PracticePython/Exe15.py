def in_text():
    return input("Give me a long text: ")


def view_text():
    tmp = in_text()
    print(tmp[::-1])


view_text()
