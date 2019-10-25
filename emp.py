import sqlite3

conn=sqlite3.connect('demo.db')
print("opened database successfully")
cursor=conn.cursor()
try:
		
    cursor.execute("""create table Employee(id INTEGER PRIMARY KEY,name Text NOT NULL,salary REAL)""")
except sqlite3.OperationalError:
    pass


print("database created successfully")



try:	
	cursor.execute("INSERT INTO Employee(id,name,salary) VALUES(1,'Paul',20000)")
	cursor.execute("INSERT INTO Employee(id,name,salary) VALUES(2,'carll',30000)")
	cursor.execute("INSERT INTO Employee(id,name,salary) VALUES(3,'rohan',40000)")
except sqlite3.IntegrityError:
	pass




conn.commit()
print("database inserted successfully")

cursor=conn.execute("SELECT id,name,salary from EMPLOYEE")
for row in cursor:
     print("ID=",row[0])
     print("NAME=",row[1])
     print("Salary=",row[2])
print("operation done successfully")


cursor.execute("UPDATE Employee set salary=10000 where id=1")

     
conn.commit()
print("database updated successfully")

cursor=conn.execute("SELECT id,name,salary from EMPLOYEE")
for row in cursor:
     print("ID=",row[0])
     print("NAME=",row[1])
     print("Salary=",row[2])
print("operation done successfully")

conn.close()


  

    
