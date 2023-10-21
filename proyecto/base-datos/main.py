# Modul import
import mysql.connector

# conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# conexion correcta? dwn1080 / 3cu4dor-1t#2
# print(database)

# cursor consultas
cursor = database.cursor(buffered=True)

# crear base de datos / comentado con """
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
    """

# crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id INT(10) AUTO_INCREMENT NOT NULL,
    marca VARCHAR(40) NOT NULL,
    modelo VARCHAR(40) NOT NULL,
    precio FLOAT(10,2) NOT NULL,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

# show table / comentadodo para q no se ejecute nuevamente """
"""
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
    """

# insertar registros / ejm. insert 1 x 1
# cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 16700)")

# insertar registros / ejm. insert varios
autos = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 12000),
    ('Citroen', 'Saxo', 4000),
    ('Mercedes', 'Clase C', 35000)
]

# comentadodo para q no se ejecute nuevamente #
# cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)", autos)

database.commit()

# listar
cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()

print("---TODOS MIS AUTOS---")
for auto in result:
    print(auto[1], auto[2], auto[3])


cursor.execute("SELECT * FROM vehiculos")
auto = cursor.fetchone()
print(auto)

# borrar datos
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault'")
database.commit()

# mirar datos borrados
print(cursor.rowcount, "borrados !!")

# actualizar
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat' ")
database.commit()

print(cursor.rowcount, "actualizados !!")