#displaying all rows of emptab
import mysql.connector as ms
#connect to mysql database
conn = ms.connect(host='localhost', database='demo1', user='root',
                       password='')

#prepare a cursor object using cursor() method
cursor = conn.cursor()

#execute a sql query using execute() method
cursor.execute("select * from stud")

#get only one row
row = cursor.fetchone()

#if the row exists
while row is not None:
    print(row)
    row = cursor.fetchone()  #get the next row

#close connection
cursor.close()
conn.close()
