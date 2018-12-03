import os
from string import punctuation
from string import whitespace


def read(filename):
    """Return contents of text file as a string."""
    with open(filename) as file:
        return file.read()


def remove_punctuation(s):
    """Return copy of s with punctuation removed."""
    for c in punctuation:
        if c in s:
            s = s.replace(c, "")
    return s


def word_counter(s):
    x = 0
    for c in whitespace:
        if c in s:
            x += 1
    return x


def index_and_search(dirname, root_path_length):
    filenames = os.listdir(dirname)
    for filename in filenames:
        path = dirname + "\\" + filename
        if os.path.isdir(path):
            index_and_search(path, root_path_length)
        elif path.endswith(".txt"):
            string = remove_punctuation(read(path))

            word_count = len(string.split())

            if word_count > 0:
                print(format(word_count, "6") + " " + path[root_path_length:])


try:

        #  search_string = input("Search string (case sensitive; hit return to cancel): ")

    root_path = os.pardir
    if os.path.isdir(root_path):
        index_and_search(root_path, len(root_path) + 1)
except OSError as err:
    print(err)
    print("Stopping, can't access files.")

print()
input("Press return to continue ...")
