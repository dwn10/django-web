import subprocess

t=1
s=""

def turnoff():
    print("\n--------------------------------")
    t=int(input("Tiempo para que se apague: "))*60
    print("\n--------------------------------")
    if t > 1:
        subprocess.call("shutdown -s -t %d" %t)
        s=str(input("Desea cancelar[s/n]: "))
        print("\n--------------------------------")

        if "s"==s:
            subprocess.call("shutdown -a")
        if "n"==s:
            pass

turnoff()