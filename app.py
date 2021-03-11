# import os
import json
import difflib
from db import collection
from db import client

from difflib import SequenceMatcher
from difflib import get_close_matches


def value(key):
    keyLower = key.lower()
    userQuery = {f"{keyLower}": {"$regex": ""}}

    capitalizeQuery = {f"{keyLower.capitalize()}": {"$regex": ""}}
    upperQuery = {f"{keyLower.upper()}": {"$regex": ""}}

    wordUpper = collection.find_one({f"{keyLower.upper()}": {"$regex": ""}})

    # This checks first the dictionary database with the user query that is in lowercase
    if (collection.find_one(userQuery)):
        wordFound = collection.find_one(userQuery)
        if (len(wordFound[keyLower][0]) == 1):
            print(f"The word '{keyLower}' has the following meaning:")
            client.close()
            return print("1. " + wordFound[keyLower])
        else:
            print(
                f"The word '{keyLower}' has '{len(wordFound[keyLower])}' meanings, which are as follows: \n")
            i = 0
            while (i < len(wordFound[keyLower])):
                print(f"{i+1}. {wordFound[keyLower][i]}")
                i += 1
            client.close()
            return
    # If word was not found through the lowercase user query then search the same query but with the word capitalized (for cities and countries)
    elif (collection.find_one(capitalizeQuery)):
        wordFound = collection.find_one(capitalizeQuery)
        if (len(wordFound[keyLower.capitalize()][0]) == 1):
            print(
                f"The word '{keyLower.capitalize()}' has the following meaning:")
            client.close()
            return print("1. " + wordFound[keyLower.capitalize()])
        else:
            print(
                f"The word '{keyLower.capitalize()}' has '{len(wordFound[keyLower])}' meanings, which are as follows: \n")
            i = 0
            while (i < len(wordFound[keyLower.capitalize()])):
                print(f"{i+1}. {wordFound[keyLower.capitalize()][i]}")
                i += 1
            client.close()
            return
    # If the capitalized word wasn't found in the dictionary, then search the same query but with the word in upper-case.
    elif (wordUpper):
        wordFound = collection.find_one(upperQuery)

        if (len(wordFound[keyLower.upper()][0]) == 1):
            print(
                f"The word '{keyLower.upper()}' has the following meaning:")
            client.close()
            return print("1. " + wordFound[keyLower.upper()])
        else:
            print(
                f"The word '{keyLower.upper()}' has '{len(wordFound[keyLower])}' meanings, which are as follows: \n")
            i = 0
            while (i < len(wordFound[keyLower.capitalize()])):
                print(f"{i+1}. {wordFound[keyLower.capitalize()][i]}")
                i += 1
            client.close()
            return
    # Last resort. If even the upper-case word wasn't found in the dictionary, then use similarity ratio to try and find the closest match.
    else:
        closeMatches = []

        # ---> This goes through the database and adds all the closest words (high similarity-ratio) to closeMatches -array
        for word in collection.find():
            closeMatch = get_close_matches(
                keyLower, word, n=1, cutoff=0.801)
            if (len(closeMatch) != 0):
                closeMatches.append(closeMatch[0])
        # <---

        # Afterwards when the for in loop is done, we'll check that the closeMatches array isn't empty
        if (closeMatches):
            # Then we'll make a query variable for the top (first) closest match in the array
            closeMatchesQuery = {f"{closeMatches[0]}": {"$regex": ""}}
            # This will be the word that the query found. If the word has one meaning, the key value is a string.
            # If the word has more than one meaning then the key value is an array of strings
            wordFound = collection.find_one(closeMatchesQuery)

            # Checks if the word has one meaning
            if (len(wordFound[closeMatches[0]][0]) == 1):
                print(
                    f"The closest match to '{key}', which we found is '{closeMatches[0]}' and that has the following meaning: \n")
                client.close()
                return print("1. " + wordFound[closeMatches[0]])
            # else the word has to have multiple meanings and we'll print them accordingly:
            else:
                print(
                    f"The closest match to '{key}', which we found is '{closeMatches[0]}' and that has '{len(wordFound[closeMatches[0]])}' meanings: \n")
                i = 0
                while (i < len(wordFound[closeMatches[0]])):
                    print(f"{i+1}. {wordFound[closeMatches[0]][i]}")
                    i += 1
                client.close()
                return
        # If there wasn't even a closest match, return nothing but a print:
        else:
            client.close()
            return print("There is no such word.")


word = input("Enter a word: ")


value(word)
