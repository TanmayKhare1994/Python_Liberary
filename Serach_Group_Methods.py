import re

pattern = r"pam"

match=re.search(pattern,"eggspamsausage")
if match:
    print match.group()    #returns matched string
    print match.start()   #where the matching string started
    print match.end()     #where the matching string ends
    print match.span()    # retrun touple of 1st match of string