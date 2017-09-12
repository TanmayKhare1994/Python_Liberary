#  more metacharacters are *, +, ?, { and }

# 1) *
import re
pattern = r"Ak*"          #irrelevent to the case
pattern1 = r"[A-Z]*"

if re.search(pattern1,"my name is ak1 , Ak1 is grate but not depend "):
    print("matched")

