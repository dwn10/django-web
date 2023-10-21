# Modul import
import sqlite3

# conexión
conexion = sqlite3.connect('test.db')

# crear cursor
cursor = conexion.cursor()

# crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio INT(255)
);
""")

# guardar cambios
conexion.commit()

# insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción de producto', '550') ")
conexion.commit()

# borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# insertar varios productos
productos =[
    ("Ordenador", "Pc", 700),
    ("Movil", "Nokia", 140),
    ("Mother Board", "Orion", 120),
    ("Tablet", "12 Inch", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

# update
cursor.execute("UPDATE productos SET precio = 620 WHERE precio = 120")

# listar datos / "SELECT * FROM productos WHERE precio >= 300;"
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print("ID:", producto[0])
    print("Titulo:", producto[1])
    print("Descripción:", producto[2])
    print("Precio:", producto[3])
    print("\n")

# cerrar conexión
conexion.close()