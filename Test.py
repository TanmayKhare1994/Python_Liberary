"""
try:
    print(1/0)
except ZeroDivisionError:
    print "ZeAkhilesh"
    raise ValueError

"""

try:
    print  1
    print 20/0
    print 2
except ZeroDivisionError:
    print 3
finally:
    print 4