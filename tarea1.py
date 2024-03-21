import os
#contenido = os.listdir('Libros')
#print(f"Las opciones de libro son: {contenido}")
#libro = input("Ingrese el libro que desea revisar:")

opcion = ""

while(opcion != "salir"):
    print("""TAREA 1
      Seleccione la opcion que desea realizar:
      1.Contador
      2.Buscar
      3.Reemplazar
      4.Salir
      """)
    opcion = input("Ingrese la funcion que desea relizar: ")
    opcion.lower()
    if opcion == "contador":
        print("contar")

    elif opcion == "buscar":
         print("bucar")

    elif opcion == "reemplazar":
         print("reemplazar")

    elif opcion == "salie":
         print("Saliendoooo") 
         break    
    
    else:
        print("Por favor selecciona una opcion correcta")
