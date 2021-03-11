# import os
import json
import difflib

from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("./Interactive English Dictionary/dictionaryData.json"))


def value(key):
    # if data.get(key):
    #     return print(data[key])
    # else:
    #     return print("There is no such word")
    keyLower = key.lower()

    closeMatches = get_close_matches(keyLower, data, n=1)

    if (keyLower in data):
        if (len(data[keyLower]) == 1):
            print(f"The word '{keyLower}' has the following meaning:")
            return print(data[keyLower])
        else:
            print(
                f"The word '{keyLower}' has '{len(data[keyLower])}' meanings, which are as follows:")
            return print(data[keyLower])
    elif (len(closeMatches)):
        if (len(data[closeMatches[0]]) == 1):
            print(
                f"The closest match to '{keyLower}', which we found is '{closeMatches[0]}' and that has the following meaning: \n")
            return print(data[closeMatches[0]])
        else:
            print(
                f"The closest match to '{keyLower}', which we found is '{closeMatches[0]}' and that has '{len(data[closeMatches[0]])}' meanings: \n")
            return print(data[closeMatches[0]])
    else:
        return print("There is no such word.")


word = input("Enter a word: ")


value(word)


# print(get_close_matches("rainn", data))

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
