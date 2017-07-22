# aways try to free up the resurce as soon as thier work is completed.

try:
    f=open("Akhilesh1.txt")
    print f.read()
except:
    print "Please insert the mode"
finally:
    f.close()

# OR Using the With block which is same  as the using block in the c#
with open("Akhilesh1.txt") as f:
    print f.readlines();