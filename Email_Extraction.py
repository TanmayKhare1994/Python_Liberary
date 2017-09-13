import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str =  "Please contact info@sololearn.com for assistance"

if re.match(pattern,str):
    print("matched")

pattern1 = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str1 = "Please contact info@sololearn.com for assistance"

match1 = re.search(pattern1, str)
if match1:
   print(match1.group())