"""
myfile=open("Akhilesh.txt","r")
cnt=myfile.read()
print cnt
myfile.close()

read the file byte by byte

myfile=open("Akhilesh.txt",'r')
print myfile.read(19)
print myfile.read(4)
print myfile.read(7)
myfile.close()

With the help of for loop and range function easy to manipulate file content

file=open("Akhilesh.txt","r")
for i in range(4):
    print (file.read(10+i),i)
file.close()



file = open("Akhilesh.txt","r")
str=file.read()
print str
print "Length of file is : ",len(str)
file.close()
"""
"""
file1=open("Akhilesh.txt","r")
print file1.readlines()
print "\n"
file1.close()

#or

file2 = open("Akhilesh.txt","r")
for line in file2:
    print line
file2.close()

"""
print  len(open("Akhilesh.txt","r").readlines()) #to find the Number of lines in the files
