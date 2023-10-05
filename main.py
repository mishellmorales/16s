#Crear un nuevo archivo llamado my_notes.txt y escribir notas en él
with open("my_notes.txt", "w") as archivo:
    archivo.write("Nota 1: saldre de compras a las 2pm.\n")
    archivo.write("Nota 2: viajare en estos dias a playas.\n")
    archivo.write("Nota 3: y finalmente regresare a mi trabajo despues de 8 dias.\n")

# Abrir el archivo my_notes.txt y leer su contenido línea por línea
with open("my_notes.txt", "r") as archivo:
    # Leer y mostrar cada línea en la consola
    for linea in archivo:
        print(linea.strip())  # strip() elimina los espacios en blanco y saltos de línea al principio y al final de cada línea

# Cerrar el archivo automáticamente al salir del bloque "with"