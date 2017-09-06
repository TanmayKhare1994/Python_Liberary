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