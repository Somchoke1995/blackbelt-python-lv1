bddict = {'Albert Einstein': '14/03/1879', 'Benjamin Franklin': '17/01/1706', 'Ada Lovelace': '10/12/1815'}

print('Welcome to the birthday dictionary. We know the birthdays of:')
for item in bddict:
    print(item)

who = input ("Who's birthday do you want to look up?")
try:
    print (who + "'s birthday is " + bddict[who])
except Exception:
    print ("Don't have " + who + " in my dictionary.")
