import re
string_ = ["aBc", "ab", "12abc55", "ABAB", "125", "aBc", "ab", "12abc55", "ABAB", "125"]

def hasNubers(inputString):
    return bool(re.search(r"\d", inputString))

for i in range(0,len(string_)-1):
    if string_[i].isalnum() and hasNubers(string_[i+1]):
        print(string_[i] + ' '+ string_[i+1])
    else:
        print()

