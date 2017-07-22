sqaures={1:1,2:3,3:4}

sqaures[4]=5 # adding key value pair
sqaures[5]=5 # adding key value pair
sqaures[5]=6 # Modifying key value pair

for i in sqaures:
    print i,sqaures[i]

#Finding wether the key is in Dictionary or not

print "\n"
print 1 in sqaures
print 6 in sqaures
print 6 not in sqaures
print "\n"
#get Method , it return None by default if not found the key and also

pairs = {2:"apple","Orange":[1,2,3],True:False,None:"True"}
# if use 1 in key here gives false & didt give you proper result.
print pairs.get(2)
print pairs.get("Orange")

# Custom message in get methord

print pairs.get(12345,"Not in Dictonary")
print pairs.get(None,"Not in Dictonary")
