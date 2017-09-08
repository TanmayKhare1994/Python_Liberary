import re

pattern =r"spam"

if re.match(pattern,"eggspameggspameggspameggspam"):
    print "Matched in Match function"
elif re.search(pattern,"eggspameggspameggspameggspam"):  #The function re.search finds a match of a pattern anywhere in the string.
    print "Matched in search Function"

#The function re.findall returns a list of all substrings that match a pattern.
print re.findall(pattern,"eggspameggspameggspameggspameggspam")