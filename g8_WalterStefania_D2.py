agenda = []

def pedir_numero():
    while True:
        try:
            valor = int(input("ingrese el numero de teléfono: "))
            return valor
        except ValueError:
            print("Debes escribir un numero: " )
            continue
        
def guardar_contacto():
    nombre = input("Dígame su nombre: ")
    numero = pedir_numero()
    print(numero)

    contacto = {
                "nombre" : nombre,
                "numero" : numero,

    }
    agenda.append(contacto)

def mostrar_opciones():
    return input("Ingrese opcion: \n1_ Agregar contacto\n2_ Buscar contacto \n Cualquier tecla (salir):_ ")

def buscar_contacto():
    nombre = input("nombre: ")
    for contacto in agenda:
        if(nombre == contacto["nombre"]):
            print("------- CONTACTO -------")
            print("Nombre: " + contacto["nombre"])
            print("Número: " + str(contacto["numero"]))
            print("------------------------\n")
            return
    print ("No se ha encontrado el nombre: "+ nombre+"\n")

opcion = mostrar_opciones()
while opcion == '1' or opcion =='2':
    if(opcion == '1'):
        guardar_contacto()
    else:
        buscar_contacto()
        
    opcion = mostrar_opciones()
print(agenda)