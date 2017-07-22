"""
print 1
raise ValueError,"Genrated by me myself"
print 2


try:
    print(1/0)
except ZeroDivisionError:
    print "ZeAkhilesh"
    raise ValueError,ZeroDivisionError


name="123"
raise NameError("Invalid Name")

"""

try:
    num=5/0
except:
    print "an error occured"
    raise