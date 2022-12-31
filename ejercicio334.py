import psycopg2

conexion1 = psycopg2.connect(database="bd1", user="postgres", password="123456")
cursor1=conexion1.cursor()
cursor1.execute("select codigo, descripcion, precio from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()