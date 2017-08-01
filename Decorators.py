# def Decor(f):
#     def Warp():
#         print ("Wrap Function")
#         f()
#         print("f function inside Wrap()")
#     return  Warp
#
# def p_ext():
#     print "p_extension function"

# p_ext = Decor(p_ext)
# print p_ext()

def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

#decorated = decor(print_text)
#decorated()
"""
Concept Not Clearned 
"""
# you can use the following statement or
@decor
def print_level():
    print "Humma"
# or
decor()


