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


print("========================================  Getter and Setter =====================================================")
#Setter and Getter

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Sw0rdf1sh!":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)