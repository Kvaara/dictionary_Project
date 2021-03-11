# import os
import json
import difflib

from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("./Interactive English Dictionary/dictionaryData.json"))


def value(key):
    keyLower = key.lower()

    closeMatches = get_close_matches(keyLower, data, n=1)

    # This checks first the dictionary with the word capitalized (To account for cities or countries)
    if (keyLower.capitalize() in data):
        if (len(data[keyLower.capitalize()]) == 1):
            print(
                f"The word '{keyLower.capitalize()}' has the following meaning:")
            return print("1. " + data[keyLower.capitalize()][0])
        else:
            print(
                f"The word '{keyLower}' has '{len(data[keyLower])}' meanings, which are as follows: \n")
            i = 0
            while (i < len(data[keyLower])):
                print(f"{i+1}. {data[keyLower][i]}")
                i += 1
            return
    elif (keyLower in data):
        if (len(data[keyLower]) == 1):
            print(f"The word '{keyLower}' has the following meaning:")
            return print("1. " + data[keyLower][0])
        else:
            print(
                f"The word '{keyLower}' has '{len(data[keyLower])}' meanings, which are as follows: \n")
            i = 0
            while (i < len(data[keyLower])):
                print(f"{i+1}. {data[keyLower][i]}")
                i += 1
            return
    elif (len(closeMatches)):
        if (len(data[closeMatches[0]]) == 1):
            print(
                f"The closest match to '{keyLower}', which we found is '{closeMatches[0]}' and that has the following meaning: \n")
            return print("1. " + data[closeMatches[0]][0])
        else:
            print(
                f"The closest match to '{keyLower}', which we found is '{closeMatches[0]}' and that has '{len(data[closeMatches[0]])}' meanings: \n")
            i = 0
            while (i < len(data[closeMatches[0]])):
                print(f"{i+1}. {data[closeMatches[0]][i]}")
                i += 1
            return
    else:
        return print("There is no such word.")


word = input("Enter a word: ")


value(word)


# print(get_close_matches("rainn", data))

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
