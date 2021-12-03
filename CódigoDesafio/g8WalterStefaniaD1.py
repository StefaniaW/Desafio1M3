nombre = input("Dígame su nombre: ")
edad_como_cadena = input("Dime tu edad: ")
edad = int(edad_como_cadena)
if edad >= 16:
    print (nombre + " puede votar")
else:
    print (nombre + " debe esperar para votar")

