from Persistencia_datos import *

if __name__ == "__main__":
 # Ejecutars
    nombre = input("Dime tu nombre")
    edad = input("Dime tu edad")
    write("tiritiri.json", {"nombre": nombre, "edad": edad})
    print(read("tiritiri.json"))
    
    clave = input("Dime una clave")
    valor = input("Que valor anadiras?")
    update("tiritiri.json", clave, valor)
    print(read("tiritiri.json"))
    
    respuesta = input("OPCIONES secundarias: 1-Read 2-Write 3-Update, 4-Clear 5-Delete 6-Salir")
    while respuesta != 6:
        if respuesta == "1":
            read("tiritiri.json")
        elif respuesta == "3":
            update("tiritiri.json")
        elif respuesta == "4":
            clear("tiritiri.json")
        elif respuesta == "5":
            delete("tiritiri.json")