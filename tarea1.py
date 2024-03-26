import os
contenido = os.listdir('Libros')
for i, libro in enumerate(contenido):
    print(f"Libro {i} : {libro}")

opcion_libro = input("Seleccione el numero del libro que desea analizar: ")
nombre_libro = contenido[int(opcion_libro)]

with open(f"Libros/{nombre_libro}", "r", encoding="UTF-8") as Archivo1:
    ContenidoArchivo1 = Archivo1.read()
    
palabra = input("Ingrese la palabra que desea buscar: ")
print(f"La palabra completa: {palabra},  sin distinción de mayúsculas y minúsculas aparece{ContenidoArchivo1.lower().replace(",","").count(palabra.lower())}")  
print(f"La palabra completa: {palabra}, con distinción de mayúsculas y minúsculas aparece{ContenidoArchivo1.replace(",","").count(palabra)}")  
print(f"La palabra o substring: {palabra}, sin distinción de mayúsculas y minúsculas{ContenidoArchivo1.lower().count(palabra.lower())}")        
print(f"La palabra o substring: {palabra}, sin distinción de mayúsculas y minúsculas{(ContenidoArchivo1.count(palabra))}")




