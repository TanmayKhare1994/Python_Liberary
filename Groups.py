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
