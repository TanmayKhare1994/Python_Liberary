#testing lambda

def my_lambda(f,x):
    return f(x)

print my_lambda(lambda x: x**3 ,3)

# lambdas aren't as powerfull as named functions

#function = 1
def polynomial(x):
    result = x**2 + 5*x
    return result

print polynomial(2)

#function = 2
print ((lambda x: x**2 +5*x) (2))
#functions 1 & 2 are equivalent

# lambdas can be assigned to the variables as follows :-

double = lambda x,y:x+y
print double(12,12)