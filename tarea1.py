import os

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','á','é','í','ó','ú']

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


contenido_libro = ContenidoArchivo1
numero_palabras_total = len(contenido_libro.split())
print(f"El número total de palabras del libro {nombre_libro} es de {numero_palabras_total}\n")

numero_palabras_no_repetidas = len(set(contenido_libro.split()))
print(f"El número de palabras no repetidas del libro {nombre_libro} es de {numero_palabras_no_repetidas}\n")


# EN LUGAR DE USAR REPLACE SE PUEDE RESTAR LA CANTIDAD DE SALTOS DE LINEA
numero_caracteres_con_espacio = len(contenido_libro)
numero_caracteres_con_espacio =  len(contenido_libro.replace("\n",""))
print(f"El número de caracteres con espacio del libro {nombre_libro} es de {numero_caracteres_con_espacio}\n")

numero_caracteres_sin_espacio = len((contenido_libro.replace(" ","")).replace("\n",""))
print(f"El número de caracteres sin espacio del libro {nombre_libro} es de {numero_caracteres_sin_espacio}\n")

numero_parrafos = contenido_libro.count("\n")
print(f"El número de párrafos del libro {nombre_libro} es de {numero_parrafos}")

numero_parrafos_2 = len(contenido_libro.splitlines()) - contenido_libro.splitlines().count("")
print(f"El número de párrafos del libro {nombre_libro} es de {numero_parrafos_2}")

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



# 1. La funcion texto_reemplazar tiene como entrada un string con el contenido del texto que se desea analizar.
# 2. Luego se solicita al usuario escribir la palabra que quiere reemplazar y luego la palabra nueva. Luego se le pide si quiere hacer distincion de mayusculas y minusculas y si es palabra completa o substring
# 3. Luego se hace una transformacion del texto en caso de no distinguir mayusculas para una mejor busqueda.
# 4. Ahora para la busqueda se hace uso del comando find junto con la variable indice_busqueda para ir iterando sobre todas la palabras.
# 5. Luego busca la primera palabra que encuentre a partir del indice y almacena los indices del inicio y final de la palabra en el string.
# 6. Luego para hacer el reemplazo primero se verifica si tiene que ser palabra completa o substring
# 7. Si es substring entonces simplemente crea un nuevo string usando el texto antes de la palabra, la palabra nueva, y el texto despues de la palabra
# 8. Si tiene que ser completa entonces verifica que los caracteres antes y despues de la palabra no sean letras, si lo son actualiza el indice de busqueda
# 9. En caso de no serlos, efectua el paso 7
# 10. Luego actualiza el texto transformado sin distincion y al terminar el bucle while, retorna el nuevo contenido como string

# Funcion para reemplazar palabras, retorna el contenido_libro reemplazado
def texto_reemplazar(contenido_libro: str) -> str:
    
    # Solicitar palabras y opciones de reemplazo
    palabra_reemplazada = input("Escribir palabra reemplazada: ")
    palabra_nueva = input("Escribir palabra nueva: ")

    distincion = input("¿Distincion de mayusculas y minusculas? (si/no): ")
    completa = input("¿Reemplazar palabra completa? (si/no): ")

    # Transformar texto para trabajar con minusculas
    contenido_sin_distincion = contenido_libro
    if distincion.lower() == "no":
        contenido_sin_distincion = contenido_sin_distincion.lower()
        palabra_reemplazada = palabra_reemplazada.lower()

    indice_busqueda = 0
    while(contenido_sin_distincion.find(palabra_reemplazada, indice_busqueda) != -1):
        inicio_palabra = contenido_sin_distincion.find(palabra_reemplazada, indice_busqueda)
        fin_palabra = contenido_sin_distincion.find(palabra_reemplazada, indice_busqueda) + len(palabra_reemplazada) - 1

        if completa.lower() == "si":
            if contenido_libro[inicio_palabra - 1].lower() not in abecedario and contenido_libro[fin_palabra + 1].lower() not in abecedario:
                contenido_libro = contenido_libro[:inicio_palabra] + palabra_nueva + contenido_libro[fin_palabra + 1:]
            else:
                indice_busqueda = fin_palabra + 1
        else:
            contenido_libro = contenido_libro[:inicio_palabra] + palabra_nueva + contenido_libro[fin_palabra + 1:]
        
        contenido_sin_distincion = contenido_libro.lower()
    
    return contenido_libro


with open(f'salida/{nombre_libro}', 'w', encoding="UTF-8") as ArchivoNuevo:
    ArchivoNuevo.write(texto_reemplazar(ContenidoArchivo1))

print(ArchivoNuevo)