import re

#ex1
pattern=r"[aeiou]"  # specific set of characters only iside the box it finds
if re.search(pattern,"Akhilesh"):
    print("match1")

if re.search(pattern,"Myth"):
    print("match2")

#ex2
pattern1 = r"[A-Z][A-Z][0-9]"       # check 1st ltter by 1st block followed others letterby the numbers.

if re.search(pattern1,"LS8"):
    print("MAtch email")