import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="informatica", port="3306")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close()