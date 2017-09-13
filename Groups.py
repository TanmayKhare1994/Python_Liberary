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

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group()) # returns the whole match
   print(match.group(0)) # match only 1st group
   print(match.group(1)) # matches only 2nd group
   print(match.group(2)) # mathes only 3rd group
   print(match.groups()) # matches all groups content from 1