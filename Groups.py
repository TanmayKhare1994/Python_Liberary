import re

pattern = r"Akhilesh(Kumar)*"

if re.search(pattern,"Akhilesh"):
    print("saved")

if re.search(pattern,"Akhilesh Kumar Kumar Kumar Kumar"):
    print("saved 1")

if re.search(pattern,"Kumar"):
    print("saved 2")


