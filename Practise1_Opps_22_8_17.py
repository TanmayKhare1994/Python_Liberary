class Dog:
    def __init__(self,name,color):
        self.name = name;
        self.color = color;

    def Add(self):
        print  "The combined strins are : " +self.name + self.color


foo = Dog("Baily","Green");

print foo.name
foo.Add();   # direct print without using the print statement.