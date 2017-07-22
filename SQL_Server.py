import pyodbc

cnxn=pyodbc.connect('Driver={SQL Server};Server=localhost;Database=db;UID=sa;PWD=Akhilesh@123')
cursor= cnxn.cursor()
cursor.execute("select * from Student")
rows = cursor.fetchall()
for row in rows:
    print row

print "\n"

cursor.execute("Select First_Name,Last_Name from student")
rows = cursor.fetchall()
for row in rows:
    print row.First_Name,row.Last_Name