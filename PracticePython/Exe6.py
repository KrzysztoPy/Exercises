def check_pali(word):
    pali_word = word[::-1]
    if word == pali_word:
        print("{} is palindrome".format(word))
    else:
        print("{} isn't palindrome".format(word))


word = input("Give me a words: ")
check_pali(word)
