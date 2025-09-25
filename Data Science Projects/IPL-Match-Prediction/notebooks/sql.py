import mysql.connector
con= mysql.connector.connect(host="localhost",port="3306",user="root",password="vaishu",database="countries")
cursor=con.cursor()
selectquery="select * from countriesworld"
cursor.execute(selectquery)
records=cursor.fetchall()
for i in records:
    print(i)
cursor.close()
con.close()