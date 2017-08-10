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
