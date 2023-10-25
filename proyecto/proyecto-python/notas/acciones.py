import notas.nota as modelo

class Acciones:
    # crear nota
    def crear(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a crear una nota...")
        
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Escribe el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")

        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")

    # mostrar nota
    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]}!! Aqui tienes tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        # for para recorrer las notas
        for nota in notas:
            print("\n*************************************")
            print(nota[2])
            print(nota[3])
            print("\n*************************************")

    # eliminar nota
    def borrar(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a eliminar notas")

        titulo = input("Introduce el titulo de la nota a eliminar: ")

        nota = modelo.Nota(usuario[0], titulo)
        
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos eliminado la nota: {nota.titulo}")

        else:
            print("No se ha eliminado la nota, prueba luego...")



