import re

pattern = r".esh"

if re.match(pattern,"Akhilesh"):
    print ("Match1")

if re.match(pattern,"Lankesh"):
    print("match2")

if re.match(pattern,"Pankaj"):
    print ("match3")
else:
    print("not matched");