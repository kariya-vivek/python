# displaying all rows of emptab V3.0
import mysql.connector as ms

# connect to MySQL database
conn = ms.connect(host='localhost', database='demo1', user='root',
                       password='')

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# execute a SQL query using execute() method
cursor.execute("select * from stud")

# get all rows
rows = cursor.fetchall()

# display the number of rows
print('Total number of rows= ', cursor.rowcount)

# display the rows from rows object
for row in rows :
    eno = row[0]
    ename = row[1]
    sal = row[2]
    print(eno, ename, sal)


# close connection
cursor.close()
conn.close()
