import json
from collections import Counter

month = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
f = "info.json"
with open(f, "r") as file:
    print("Opening file ",f)
    bddict = json.load(file)
i = []
for item in bddict.keys():
    monthstr = month[str(int(bddict[item].split("/")[1]))]
    i.append(monthstr)

c = Counter(i)
print(c)
