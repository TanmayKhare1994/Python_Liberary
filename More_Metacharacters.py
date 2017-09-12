#  more metacharacters are *, +, ?, { and }

# 1) * => * matches 0 or more occurrences of the preceding expression.
import re
pattern = r"Ak*"          #irrelevent to the case
pattern1 = r"[A-Z]*"
pattern3 = r"g*"
if re.search(pattern1,"my name is ak1 , Ak1 is grate but not depend "):
    print("matched")

if re.search(pattern,"hello tango charle"):
    print("hummm ok")

if re.search(pattern3,"Akhilesh "):
    print("Matched pattern 3 *")


# 2) + => + matches 1 or more occurrence of the preceding expression.
pattern2= r'A+'
pattern4 = r"g+"

if re.search(pattern2,"A is the p and ps is the g of d what is dof a"):
    print("Match +")

if re.search(pattern4,"Akhilesh g"):
    print("Matched pattern 4 +")

# xample 1 or more 42's

pattern5 = r"(42)+$"

if re.search(pattern5,"42"):
    print("42's")

if re.search(pattern5,"424242"):
    print("42's")