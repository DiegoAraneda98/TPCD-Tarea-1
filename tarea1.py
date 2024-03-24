import os
contenido = os.listdir('Libros')
for i, libro in enumerate(contenido):
    print(f"Libro {i} : {libro}")

opcion_libro = input("Seleccione el numero del libro que desea analizar: ")
nombre_libro = contenido[int(opcion_libro)]

with open(f"Libros/{nombre_libro}", "r", encoding="UTF-8") as Archivo1:
    ContenidoArchivo1 = Archivo1.read()
    
palabra = input("Ingrese la palabra que desea buscar: ")
print(ContenidoArchivo1.lower().count(palabra.lower()))        
print((ContenidoArchivo1.count(palabra)))
print(ContenidoArchivo1.lower().find(palabra))  
print(ContenidoArchivo1.find(palabra))  



