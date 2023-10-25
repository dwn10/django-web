import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    def __init__(self, usuario_id, titulo = "", descripcion = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    # guardar
    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        database.commit()
        # cantidad de filas afectadas
        return [cursor.rowcount, self]
    
    # listar
    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    # eliminar
    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%' "

        cursor.execute(sql)
        # hacer cambios en bases de datos
        database.commit()
        # cantidad de filas afectadas
        return [cursor.rowcount, self]
