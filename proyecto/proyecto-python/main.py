"""
Proyecto Python & MySQL:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la BD
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas...
"""

from usuarios import acciones

print("""
Acciones disponibles:
      - registro (r)
      - login (l)
""")

hazEl = acciones.Acciones()
accion = input("Que quieres hacer?:")

if accion == "r":
    hazEl.registro()

elif accion == "l":
    hazEl.login()
