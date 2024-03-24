import os
contenido = os.listdir('Libros')
for i, libro in enumerate(contenido):
    print(f"Libro {i} : {libro}")

opcion = input("Seleccione el numero del libro que desea analizar: ")
nombre_libro = contenido[int(opcion)]

with open(f"Libros/{nombre_libro}", "r", encoding="UTF-8") as Archivo1:
    ContenidoArchivo1 = Archivo1.read()

# opcion = ""

# while(opcion != "salir"):
#     print("""TAREA 1
#       Seleccione la opcion que desea realizar:
#       1.Contador
#       2.Buscar
#       3.Reemplazar
#       4.Salir
#       """)
#     opcion = input("Ingrese la funcion que desea relizar: ")
#     opcion.lower()
#     if opcion == "contador":
#         print("contar")

#     elif opcion == "buscar":
#          print("bucar")

#     elif opcion == "reemplazar":
#          print("reemplazar")

#     elif opcion == "salie":
#          print("Saliendoooo")
#          break

#     else:
#         print("Por favor selecciona una opcion correcta")
