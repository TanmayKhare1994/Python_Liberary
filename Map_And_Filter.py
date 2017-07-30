def add_func(x):
    return x+10

numbers=[12,23,34,45,56,23]

result = list(map(add_func,numbers))
print result
print "\n"
# command tasks that you want to perform in list use map
"""
The built-in functions map and filter are very useful higher-order functions that 
operate on lists (or similar objects called iterables). 
The function map takes a function and an iterable as arguments,
and returns a new iterable with the function applied to each argument. 
"""

# we can also use lambda

print list(map(lambda x:x+10 , numbers))


# Filter :- The function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).
print list(filter(lambda x: x<20 ,numbers))
res = list(filter(lambda x: x%2==0, numbers))
print(res)