# class Dog:
#     def Body(self,height,color,beh):
#         self.height = height;
#         self.color = color;
#         self.beh = beh;
#         print

print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

# class Animals:
#
#     def Wild(self,name,no):
#         self.name = name;
#         self.no = no;
#         for i in range(1,15,2):
#             print i;
#
# obj = Animals();
# obj.Wild("JK Rolings",56);


print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)