import json
import os

data = json.load(open("./Interactive English Dictionary/dictionaryData.json"))


def value(key):
    # if data.get(key):
    #     return print(data[key])
    # else:
    #     return print("There is no such word")
    if key in data:
        return print(data[key])
    else:
        return print("There is no such word.")


word = input("Enter a word: ")

value(word)

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
