import subprocess

t=1
s=""

# Mostrar mensaje de ayuda
print("\n * Introduzca el Tiempo en minutos.")
print(" * Para apagar el sistema")

def turnoff():
    print("--------------------------------")
    t=int(input("Tiempo para que se apague: "))*60
    print("--------------------------------")
    if t > 1:
        subprocess.call("shutdown -s -t %d" %t)
        s=str(input("Desea cancelar[s/n]: "))
        print("--------------------------------")

        if "s"==s:
            subprocess.call("shutdown -a")
        if "n"==s:
            pass

turnoff()