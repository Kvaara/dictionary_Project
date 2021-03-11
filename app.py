import json
import os

data = json.load(open("./Interactive English Dictionary/dictionaryData.json"))


def value(key):
    # if data.get(key):
    #     return print(data[key])
    # else:
    #     return print("There is no such word")

    keyLower = key.lower()
    i = 0
    while i < len(keyLower):
        i += 1
        if keyLower[:i] in data:
            if i < len(keyLower):
                print(
                    f"The closest word we found for your search was '{keyLower[:i]}'.")
                return print(data[keyLower[:i]])
            else:
                print(f"What does '{keyLower[:i]}' mean?")
                return print(data[keyLower[:i]])
        print(i)
        print(keyLower[:i])
    else:
        return print("There is no such word.")

        # if keyLower[:i] in data:
        #     return print(data[keyLower])
        # else:
        #     return print("There is no such word.")


word = input("Enter a word: ")

value(word)

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
