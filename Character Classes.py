import re

#ex1
pattern=r"[aeiou]"  # specific set of characters only iside the box it finds
if re.search(pattern,"Akhilesh"):
    print("match1")

if re.search(pattern,"Myth"):
    print("match2")

#ex2
pattern1 = r"[A-Z][A-Z][0-9]"       # check 1st ltter by 1st block followed others letterby the numbers.
pattern2 = r"[A-Za-z][0-9]"
pattern3 = r"[^A-Z]"

if re.search(pattern1,"LS8"):
    print("MAtch email");

if re.search(pattern2,"Akhileshsh026"):
    print("Correct USername");

if re.search(pattern3,"9087"):
    print("pattern 3 matched");


if re.search(pattern3, "this is all quiet"):  #except capital lettrs there are other cases too
    print("pattern 3 matched");

if re.search(pattern3, "AbCdEfG123"):           #mixer
    print("pattern 3 matched");

if re.search(pattern3, "THISISALLSHOUTING"): #all cpas not allowed
    print("pattern 3 matched");
else:
    print("pattern not  3 matched");