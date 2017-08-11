class Animal:
    def __init__(self,color,legs):
        self.color=color;
        self.legs=legs;

class Dog(Animal):
     def bark(self):
         print "\n "+self.color + " " + str(self.legs) + " " + "Dog Barks";

class Cat(Animal):
    def Miyon(self):
        print "\n" +self.color + " " + self.legs + " " + "Cat didn't Barks";

Doga_Obj = Dog("Brown",4);
Cata_obj= Cat("black","4");

print Doga_Obj.color+" "+str(Doga_Obj.legs),Doga_Obj.bark(),"\n";
print Cata_obj.color + " "+Cata_obj.legs , Cata_obj.Miyon();

print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

print "\t \t Inheritance can also be indirect. One class can inherit from another, and that class can inherit from a third class \t \t ";
print "\n"

class A:
    def method(self):
        print("A method")


class B(A):
    def another_method(self):
        print("B method")


class C(B):
    def third_method(self):
        print("C method")


c = C()
c.method()
c.another_method()
c.third_method()


print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "\n"
print "\t \t function super : \t \t"

class D(A):
    def method(self):
        print ("Class D");
       # super(A, self).method();  # not working in py 3.0 it is super.method();
