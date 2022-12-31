import sqlite3

class Articulos:

    def abrir(self):
        conexion=sqlite3.connect("bd1.db")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion, precio) values (?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select descripcion, precio from articulos where codigo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo, descripcion, precio from articulos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from articulos where codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    def modificacion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update articulos set descripcion=?, precio=? where codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()