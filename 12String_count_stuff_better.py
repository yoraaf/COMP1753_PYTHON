from string import punctuation
from string import whitespace
from string import digits
from string import ascii_letters


def remove_punctuation(s):
    """Return copy of s with punctuation removed."""
    for c in punctuation:
        if c in s:
            s = s.replace(c, "")
    return s


def remove_whitespace(s):
    """Return copy of s with whitespace removed."""
    for c in whitespace:
        if c in s:
            s = s.replace(c, "")
    return s


def make_alphanumeric(s):
    """Return copy of s with only alphanumeric characters."""
    for character in s:
        if character.isalnum() is False:
            s.replace(character, "")
    return s


def count_letters(s):
    x = 0
    for character in s:
        if character in ascii_letters:
            x += 1
    return x


def count_digits(s):
    x = 0
    for character in s:
        if character in digits:
            x += 1
    return x


def count_whitespaces(s):
    x = 0
    for character in s:
        if character in whitespace:
            x += 1
    return x


def count_punctuation(s):
    x = 0
    for character in s:
        if character in punctuation:
            x += 1
    return x


def count_string_anything(s, option):
    """
    :param s: A string to count things in
    :param option: 0 for letters, 1 for digits, 2 for whitespaces, 3 for punctuation
    :return: The amount of chosen things in the string
    """
    options = [ascii_letters, digits, whitespace, punctuation]
    x = 0
    for character in s:
        if character in options[option]:
            x += 1
    return x


string = "Hello, COMP1753!! How are you doing today?"
print(string)
print(format(count_string_anything(string, 0), ">4")+" letters")
print(format(count_string_anything(string, 1), ">4")+" digits")
print(format(count_string_anything(string, 2), ">4")+" whitespaces")
print(format(count_string_anything(string, 3), ">4")+" punctuation")
print(format(len(string), ">4")+" total")

print()
input("Press return to continue ...")
