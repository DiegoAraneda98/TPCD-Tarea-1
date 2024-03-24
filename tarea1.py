import os

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

contenido = os.listdir('Libros')
for i, libro in enumerate(contenido):
    print(f"Libro {i} : {libro}")

opcion = input("Seleccione el numero del libro que desea analizar: ")
nombre_libro = contenido[int(opcion)]

with open(f"Libros/{nombre_libro}", "r", encoding="UTF-8") as Archivo1:
    ContenidoArchivo1 = Archivo1.read()
#   print(ContenidoArchivo1)
# print((ContenidoArchivo1.split()))
print(len(ContenidoArchivo1.split()))
print(len(set(ContenidoArchivo1)))
print(len(ContenidoArchivo1))
print(len(ContenidoArchivo1.replace(" ","")))
print(len(ContenidoArchivo1.split("\n")))

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

def texto_reemplazar(contenido_libro: str) -> str:
# Funcion para reemplazar palabras, retorna el contenido_libro reemplazado

    palabra_reemplazada = input("Escribir palabra reemplazada: ")
    palabra_nueva = input("Escribir palabra nueva: ")
    
    distincion = input("¿Distincion de mayusculas y minusculas? (si/no): ")
    completa = input("¿Reemplazar palabra completa? (si/no): ")
    
    contenido_sin_distincion = contenido_libro
    if distincion.lower() == "no":
        contenido_sin_distincion = contenido_libro.lower()
        palabra_reemplazada = palabra_reemplazada.lower()
    
    indice_busqueda = 0
    while(contenido_sin_distincion.find(palabra_reemplazada, indice_busqueda) != -1):
        inicio_palabra = contenido_sin_distincion.find(palabra_reemplazada, indice_busqueda)
        fin_palabra = contenido_sin_distincion.find(palabra_reemplazada, indice_busqueda) + len(palabra_reemplazada) - 1            
        if completa.lower() == "si":
            if contenido_libro[inicio_palabra - 1].lower() not in abecedario and contenido_libro[fin_palabra + 1].lower() not in abecedario:
                contenido_libro = contenido_libro[0:inicio_palabra] + palabra_nueva + contenido_libro[fin_palabra + 1:len(contenido_libro)]
                contenido_sin_distincion = contenido_libro.lower()
            else:
                indice_busqueda = fin_palabra
        else:
            contenido_libro = contenido_libro[0:inicio_palabra] + palabra_nueva + contenido_libro[fin_palabra + 1:len(contenido_libro)]
            contenido_sin_distincion = contenido_libro.lower()
    return contenido_libro




print(texto_reemplazar(ContenidoArchivo1))