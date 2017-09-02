# List Sample
Words = ["english","Hindi","!"]
print (Words[0])
print (Words[2])

print ("++++++++++++++++++++++++++")

# Empty List
Empty_List=[]
print (Empty_List)

print ("++++++++++++++++++++++++++")

for items in Words:
    print (items)

print ("++++++++++++++++++++++++++")
#List Complax

num =3
Hybd_List=["Akhilesh",12,23,343,["BMW","AUDI","Mercedece AMG"],num]

print (Hybd_List[4][2])

print ("++++++++++++++++++++++++++")
#INdexing

str="Akhilesh"
print (str[3])

print ("++++++++++++++++++++++++++")
#Assiging the Value Externlly in the List.

Words.append(23)
Words[4]="AMG"
print (len(Words))

