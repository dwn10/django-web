print()
print("      ::::::::::       ::::::::                          :::::::::::   :::::::::::   ")
print("      :+:             :+:    :+:                             :+:           :+:       ")
print("     +:+             +:+                                    +:+           +:+        ")
print("    +#++:++#        +#+             +#++:++#++:++          +#+           +#+         ")
print("   +#+             +#+                                    +#+           +#+          ")
print("  #+#             #+#    #+#                             #+#           #+#           ")
print(" ##########       ########                          ###########       ###            ")

print()

# Print the information about the open ports
#-----------------------
#  -v (vision general) | -sS () | -sV (scan version) |-sC (scan scripts) | -A (scan agresiv) |-O (scan OS) |
#-----------------------
import nmap

scanner= nmap.PortScanner()
scanner.scan('104.26.0.24', '1-1024', '-v -sS -sV -sC -A -O')

for host in scanner.all_hosts():
    print("Host: ", host)
    for proto in scanner[host].all_protocols():
        lport = scanner[host][proto].keys()
        for port in lport:
            print("   Port: ", port)
            print("   Name: ", scanner[host][proto][port]['name'])
            print("   State: ", scanner[host][proto][port]['state'])
            print("   Version: ", scanner[host][proto][port]['version'])
            if 'product' in scanner[host][proto][port]:
                print("   Product: ", scanner[host][proto][port]['product'])
            if 'extrainfo' in scanner[host][proto][port]:
                print("   Extra Info: ", scanner[host][proto][port]['extrainfo'])






import nmap
scanner = nmap.PortScanner()
scanner.scan('104.26.0.24', '1-1024')
print(scanner['104.26.0.24'].state())
print(scanner['104.26.0.24'].all_protocols())
print(scanner['104.26.0.24'] ['tcp'].keys ())


