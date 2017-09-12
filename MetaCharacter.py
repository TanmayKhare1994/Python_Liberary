import re

pattern = r"A.h" # when the word is between A and H no matter how may vharacter

if re.match(pattern,"Akhilesh"):
    print ("Match1")

if re.match(pattern,"Lankesh"):
    print("match2")

if re.match(pattern,"Pankaj"):
    print ("match3")
