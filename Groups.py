import re

pattern = r"Akhilesh(Kumar)*"

if re.search(pattern,"Akhilesh"):
    print("saved")

if re.search(pattern,"Akhilesh Kumar Kumar Kumar Kumar"):
    print("saved 1")

if re.search(pattern,"Kumar"):
    print("saved 2")

#example ^ excluding any of the vowel inside the bracket
pattern2 = '([^aeiou][aeiou][^aeiou])+'

if re.search(pattern2,"bab"):
    print("Sucess")

#groups

import re

pattern3 = r"a(bc)(de)(f(g)h)i"
pattern4 = r"(a-z,A-Z)(@)(a-z)(.)(a-z)"

match = re.match(pattern3, "abcdefghijklmnop")
if match:
   print(match.group()) # returns the whole match
   print(match.group(0)) # match only 1st group
   print(match.group(1)) # matches only 2nd group
   print(match.group(2)) # mathes only 3rd group
   print(match.groups()) # matches all groups content from 1

match1 = re.match(pattern4,"akhileshsh@hotmail.com")  # not done
if match1:
   print(match1.group()) # returns the whole match
   print(match1.group(0)) # match only 1st group
   print(match1.group(1)) # matches only 2nd group
   print(match1.group(2))

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 1st group is named group and 2nd group is non capturing group
pattern5 = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern5, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

pattern6 = r"(a)(b(?:c)(d)(?:e))"
match = re.match(pattern6, "abcde")
if match:
       print(len(match.groups()))


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

pattern7 = r"gr(a|e)y"   # | means or a or e

match = re.match(pattern7, "gray")
if match:
   print ("Match 1")

match = re.match(pattern7, "grey")
if match:
   print ("Match 2")

match = re.match(pattern7, "griy")
if match:
    print ("Match 3")


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

pattern8 = r"(.+) \1"


if re.match(pattern8,"kumar kumar sahu"):  # unlimited times the same word but 2 times back to back
    print("true")

match11 = re.match(pattern8, "?! ?!")
if match11:
   print("true 2")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

pattern9 = r"(.+)(.+)"
if re.match(pattern9,"Akhilesh Akhilesh"):
    print("Matched pattern9")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

pattern10 = r"(\D+\d)"

match12 = re.match(pattern10, "Hi 999!")

if match12:
   print("Match 1")

match13 = re.match(pattern, "1, 23, 456!")
if match13:
   print("Match 2")

match14 = re.match(pattern, " ! $?")
if match14:
    print("Match 3")


# (\D+\d) matches one or more non-digits followed by a digit.
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


pattern20 = r"\b(cat)\b"

match15 = re.search(pattern20, "The cat sat!")
if match15:
   print ("Match 1")

match15 = re.search(pattern20, "We s>cat<tered?")
if match15:
   print ("Match 2")

match15 = re.search(pattern20, "We scattered.")
if match15:
   print ("Match 3")