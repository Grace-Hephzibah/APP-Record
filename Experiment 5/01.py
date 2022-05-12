import sqlite3
# connect to a database
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute("DROP TABLE COMPANY")

# To Create a table
import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute('''CREATE TABLE COMPANY (ID INT PRIMARY KEY NOT NULL,
 NAME TEXT NOT NULL,
 AGE INT NOT NULL,
 ADDRESS CHAR(50),
 SALARY REAL);''')
print("Table created successfully")
conn.close()
       
# To insert records into a table
import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (1, 'Paul', 32, 'California', 20000.00 )");
39
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
conn.commit()
print ("Records created successfully")
conn.close()
       
# To display the data from the table
import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")   
print("Operation done successfully")
conn.close()
       
# To display all columns from a database
import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE COMPANY12345
 (ID INT PRIMARY KEY NOT NULL,
 NAME TEXT NOT NULL,
 AGE INT NOT NULL,
 ADDRESS CHAR(50),
 SALARY REAL);''')
print("Table created successfully")
conn.execute("INSERT INTO COMPANY12345 (ID,NAME,AGE,ADDRESS,SALARY)\
 VALUES (1, 'Paul', 32, 'California', 20000.00 )")
conn.execute("INSERT INTO COMPANY12345 (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
conn.execute("INSERT INTO COMPANY12345 (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
conn.execute("INSERT INTO COMPANY12345 (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
conn.commit()
print("Records created successfully")
cursor = conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY from COMPANY12345")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE=", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4])
print("Operation done successfully");
conn.close()
                      
# To update the table
import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")
print("Operation done successfully")
conn.close()

# To perform delete operation
import sqlite3
conn = sqlite3.connect('test.db')
print( "Opened database successfully")
conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")
print("Operation done successfully")
conn.close()
