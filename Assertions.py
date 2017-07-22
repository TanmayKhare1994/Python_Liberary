"""
temp= 10
assert (temp<=0),("Colder than Absolute Zero")
print temp


import math

def MyFofX(x):
    try:
     assert (x>0),"Error please enter the number grater than zero"  #it will not work with try and Except block will execute
     print math.sqrt(x)
    except:
     print("Except Block Executed")


MyFofX(9)
"""

def MyFoofX1(x):
    assert (x<0),"Enter the Number smaller than 0"
    print (x)

MyFoofX1(9)