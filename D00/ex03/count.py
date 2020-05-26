import sys
import string

argvArray = sys.argv


def text_analyzer(*args):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """

    if len(args) == 0:
        str_input = input("What is the text to analyse? ")
    elif len(args) == 1:
        str_input = args[0]
    else:
        print("ERROR")
        return

    n_char = 0
    n_upper = 0
    n_lower = 0
    n_punct = 0
    n_space = 0

    for char in str_input:
        n_char += 1
        if char.isupper():
            n_upper += 1
        elif char.islower():
            n_lower += 1
        elif char in string.punctuation:
            n_punct += 1
        elif char.isspace():
            n_space += 1
    print(
        "The text contains " + str(n_char) + " characters: \n\n" +
        "- " + str(n_upper) + " upper letters\n\n" +
        "- " + str(n_lower) + " lower letters\n\n" +
        "- " + str(n_punct) + " punctuation marks\n\n" +
        "- " + str(n_space) + " spaces")
    return
