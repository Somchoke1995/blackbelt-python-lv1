import json

with open("info.json", "r") as f:
    bddict = json.load(f)

print("Welcome to the birthday dictionary. We know the birthdays of:")
for item in bddict:
    print(item)

while True:
    who = input ("Who's birthday do you want to look up?")
    if who == "exit":
        break
    elif who == "add":
        name = input("Enter name: ")
        date = input("Enter date: ")
        bddict[name] = date
        with open("info.json", "w") as file:
            json.dump(bddict, file)
    else:
        try:
            print (who + "'s birthday is " + bddict[who])
        except Exception:
            print ("Don't have " + who + " in my dictionary.")
