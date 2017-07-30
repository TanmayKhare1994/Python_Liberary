"""
ctl + /  comment shortcut

Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices,
but they can still be iterated through with for loops.
They can be created using functions and the yield statement.

Due to the fact that they yield one item at a time,
generators don't have the memory restrictions of lists.

In short, generators allow you to declare a function that behaves like an iterator,
 i.e. it can be used in a for loop.
"""


def Countdown():
    i = 5
    while i>0:
        yield i
        i-=1

for i in Countdown():
    print(i)

# def infi():
#     while True:
#         yield 7
#
# for i in infi():
#     print i

# convert the Genrators into list
def numb(x):
    for i in range(x):
        yield i

print list(numb(11))

"""
Using generators results in improved performance, which is the result of the lazy (on demand) generation of values, 
which translates to lower memory usage. 
Furthermore, we do not need to wait until all the elements have been generated before we start to use them.
"""

def m_w():
    word=""
    for c in "Sperm":
        word+=c
        yield word

print (list(m_w()))