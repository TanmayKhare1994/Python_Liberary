print "************* Welcome to Python Calculator *******************************"
print "\n"
print "1. Add";
print "2. Substract"
print "3. Multiply"
print "4. Divide"
print "5. Reaminder"

input=float(raw_input("Please Enter your choice"))
input1= float (raw_input("Enter the no 1"))
input2= float(raw_input("Enter the no 2"))
if input==1:
    print input1+input2;
elif input==2:
    print input1-input2;
elif input==3:
    print input1*input2;
elif input==4:
    print input1//input2;
elif input==5:
    print  input1%input2;
else:
    print "You Entered Wrong Choice"
