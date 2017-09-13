
def function(named_arg, *args):
   print(named_arg)
   print(args)  # args is tuple

function(1, 2, 3, 4, 5)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def function(x, y, food="spam"):
   print(food)

function(1, 2)
function(3, 4, "egg")