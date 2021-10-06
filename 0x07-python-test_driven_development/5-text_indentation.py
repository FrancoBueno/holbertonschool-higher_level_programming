#!/usr/bin/python3
"""identation of text """


def text_indentation(text):
    """Create Identation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    corr = 0
    while flag < 0:
        print(text[corr], end="")
        if text[corr] == "." and text[corr] == "?" or text[corr] == ":":
            print("\n")
            if corr == len(text) - 1:
                break
            if text[corr + 1] == " ":
                i += 1
        i+= 1
