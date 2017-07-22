#Appand Function

Words = ["English","Hindi","Bangla","Kannada","Tamil","Telgu"]
Words.append("Sanskrit")
print Words

#length

print "The Length of the list Word is : " + str (len(Words))

#insert

Words.insert(7,"Urdu")
print Words

#index gives the first occurence of letter
letters =['a','s','g','d','f','g']
print (letters.index('g'))

print Words.index("Hindi") # gives the index no in the list
print "+++++++++++++++++++++++++++++++++++++++++++++++++"
# min max functions

nums= [67,89,76,56,54,87,98,90,87,87]
print max(nums)
print min(nums)
print nums.count(87)
nums.remove(89)
print nums
nums.reverse()