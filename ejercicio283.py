import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="informatica")
cursor1=conexion1.cursor()
sql="create database bd2"
cursor1.execute(sql)

sql="use bd2"
cursor1.execute(sql)

sql="""create table usuarios (
         nombre varchar(30) primary key,
         clave  varchar(30)
   )"""
cursor1.execute(sql)    

conexion1.commit()
conexion1.close()