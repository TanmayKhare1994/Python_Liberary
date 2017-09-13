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
pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


