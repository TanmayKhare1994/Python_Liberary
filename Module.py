#simple import usecase
import random;

for i in range(5):
    val= random.randint(0,4)
    print val

# importing specific function
from math import pi,sqrt;

print pi

#import under different namespace
from math import sqrt as SqaureRoot

print SqaureRoot(100)


def print_num(x):
    for i in range(x):
        print i;
        return

print_num(10)