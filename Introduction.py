def appy_t(func,x):
    print func(x);

def appy_t2(x):
    return x*x*x

appy_t(appy_t2,2)

#pure functions :- depends upon the the value of arguments

def purefofF(x,y):
    temp= x+(2*y)
    return temp//2

print purefofF(1,2)

#impure Function :- that does not depend upon the value of the arguments.

sample_list=[]

def impurefofF():
    sample_list.append("akhilesh")
    sample_list.append("Kumar")
    sample_list.append("sahu")
    for i in sample_list:
     print i

impurefofF()


"""
NOTE :- 

Using pure functions has both advantages and disadvantages. 
Pure functions are:
- easier to reason about and test.
- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
- easier to run in parallel.

The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task of I/O, since this appears to inherently require side effects. 
They can also be more difficult to write in some situations
"""