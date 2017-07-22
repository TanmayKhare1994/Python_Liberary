"""
file= open("Akhilesh.txt","a")
file.write("The data written by the help of python language. \n")
file.close()
"""
# print open("Akhilesh.txt","r").readlines() or pretty way
"""
file1= open("Akhilesh.txt","r")
for lines in file1:
    print lines
file1.close()

file2=open("Akhilesh1.txt","w")
file2.write("This is again new line by using python.")
file2.close()

file1= open("Akhilesh1.txt","r")
for lines in file1:
    print lines
file1.close()
"""

#using write Method who written the numbrer of bytes written to file, if sucessfull.

file3=open("Akhilesh1.txt","w")
amount_written = file3.write("Hello World!!")
if amount_written==len("Hello World!!"):
    print (amount_written)
print "Finish Operation"
file3.close()
