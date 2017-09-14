
def function(named_arg, *args):
   print(named_arg)
   print(args)  # args is tuple

function(1, 2, 3, 4, 5)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def function(x, y, food="spam"):
   print(food)

function(1, 2)
function(3, 4, "egg")


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def function1(x,y,food="paneer",**kwargs):
    print(kwargs)

print(function1(1,2,k=1,j=2,l=3))