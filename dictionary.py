import json
#from difflib import SequenceMatcher
from difflib import get_close_matches

print("Welcome to dictionary app")

data = json.load(open("data.json"))        

def getDefinition(word):

    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        closest = get_close_matches(word, data.keys())[0]
        flag = input("Did you mean this word %s? (Y/N)" % closest)
        if flag.lower() == "y":
            return data[closest]
        elif flag.lower() == "n":
            return "Word doesn't exist"
        else:
            return "Lern to write Y or N :)"
    else:
        return "Unknown word"

def nicePrint(val):
    if type(val) == list:
        num = 1
        for item in val:
            print("%s. %s" % (num,item))
            num += 1
    else:
        print(val)

word = input("Write word you want to find: ")
nicePrint(getDefinition(word))


