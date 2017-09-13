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


pattern2 = r"(4{5,6})\1"
if re.search(pattern2,"444444444444"): #10 or 12
    print("ho gya")