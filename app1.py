import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def Translate(w):
    original_word = w
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        ch = input("Did you mean %s instead ?\n Enter Y(Yes) or N(No) : " %get_close_matches(w,data.keys())[0])
        ch = ch.lower()
        if ch == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif ch == "n":
            return original_word + " doesn't exist in the Dictionary. Please double check"
        else:
            return "We didn't understand your query"
    else:
        return original_word + " doesn't exist in the Dictionary. Please double check"

word = input("\nEnter word : ")
output = Translate(word)

i = 1
if type(output) == list:
    for item in output:
        print("Definition %s : %s" %(i,item))
        i += 1
else:
    print(output)
