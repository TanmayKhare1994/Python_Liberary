try:
    num1=9;
    num2=0;
    num3=num1//num2;
except ZeroDivisionError:
    print "Due to Division by zero."
except (ValueError, TypeError):
    print "please Correct u r syntax"


try:
    input = raw_input("Enter the Number");
    print float(input)%3;
except:
    print "Please enter the numeric number"