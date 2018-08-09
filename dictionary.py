import json

print("Welcome to dictionary app")

data = json.load(open("data.json"))

word = input("Write word you want to find: ")

if word in data:
    print(data[word])
else:
    print("Incorect word")


