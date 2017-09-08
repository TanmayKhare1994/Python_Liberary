import  re

pattern = r"Akhilesh"

if(re.match(pattern,"AkhileshKumarSahu AkhileshKumarSahu")):
    print ("MAtched")
else:
    print ("Not Matched")