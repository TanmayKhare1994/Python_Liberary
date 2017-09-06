#One common use of a property is to make an attribute read-only.
class Pizza:
    def __init__(self,toppings):
        self.toppings = toppings;

    @property
    def pine_Apple(self):
        return  False

pizza =Pizza(["Cheese","Tommato"])
print(pizza.pine_Apple)

# pizza.pine_Apple =True;  this will not work

# till didn't get how to use propperties in python
class Chk_age:
    def __int__(self,age):
        self.age= age;

    @property
    def isage(self):
        if(self.age>18):
         return  "Adult"
        else:
            return "Under age"

