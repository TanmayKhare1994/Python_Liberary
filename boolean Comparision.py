from __builtin__ import raw_input

my_bolean= True

print (my_bolean)

print (45!=65)

# ifelse

inn = int(raw_input("Enter number"))
if(inn<5):
    print ("Numer is less than 5 :"+str(inn))
elif(inn>100):
    print ("Number is grater than 100")
else:
    print ("Please enter the number")

# opertion 2
if not True:
    print ("1")
elif not(1+1==3):
    print ("2")
else:
    print ("3")
