
import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")

        nombre = input("Cual es tu nombres?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Introduce tu email?: ")
        password = input("Introduce tu contraseña?: ")

        # crear usuario
        usuario = modelo.Usuario(nombre, apellidos, email, password)

        # registrar en bases de datos
        registro = usuario.registrar()

        # comprobar si esta un usuario registrado
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email} ")
        else:
            print("\nNo te has registrado correctamente!")

    def login(self):
        print("\nVale!! Identificate en el sistema...")

        try:
            email = input("Introduce tu email?: ")
            password = input("Introduce tu contraseña?: ")

            # datos a traer
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto!!! intentalo más tarde")

    # PROXIMAS ACCIONES
    def proximasAcciones(self, usuario):
        print("""
        Acciones deisponibles:
        - Crear nota (c)
        - Mostrar tus notas (m)
        - Eliminar nota (e)
        - Salir (s)
        """)
        
        # acciones
        accion = input("Que quieres hacer ?:")
        hazEl = notas.acciones.Acciones()

        # crear
        if accion == "c":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        # mostrar
        elif accion == "m":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        # eliminar
        elif accion == "e":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        # salir
        elif accion == "s":
            print(f"\nOk {usuario[1]}, hasta pronto!!!")
            exit()

    

