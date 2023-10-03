"""Module contains text_indentation function"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each
    of these characters: ., ? and :
    Args:
        text (str): text to indent
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    delim = [".", "?", ":"]
    new_line = 1
    for i in text:
        if i in delim:
            new_line = 1
            print(i, end="")
            print("\n")
            continue
        if new_line == 1 and i == " ":
            continue
        else:
            new_line = 0
        print(i, end="")
