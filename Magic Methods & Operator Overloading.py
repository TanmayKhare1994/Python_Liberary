"""
    Magic methods are special methods which have double underscores at the beginning and end of their names.
They are also known as dunders.
So far, the only one we have encountered is __init__, but there are several others.
They are used to create functionality that can't be represented as a normal method.

One common use of them is operator overloading.
This means defining operators for custom classes that allow operators such as + and * to be used on them.
An example magic method is __add__ for +.
"""

class Vector2D():
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
    def __add__(self, other):
        return Vector2D(self.x+other.x,self.y+other.y)

f1 = Vector2D(2,3);
f2= Vector2D(4,5);
result = f1+f2;
print result.x;
print result.y;

print   (":".join(["spam","12","jk","adad","23.34"]))
