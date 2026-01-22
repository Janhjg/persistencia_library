from Persistencia_datos import *

if __name__ == "__main__":
 # Ejecutars
    write("tiritiri.json", {"nombre": "Juan", "edad": 25})
    print(read("tiritiri.json"))
    update("tiritiri.json", "ciudad", "Sevilla")
    print(read("tiritiri.json"))
    clear("tiritiri.json")
    print(read("tiritiri.json"))
    
    respuesta = input("Borrar archivo json si or no: ")
    if respuesta == "si":
        delete("tiritiri.json")
    else:
        print("tas to loco")