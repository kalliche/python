import os

# file handling (nanejo de ficheros)
# .txt file

txt_file = open(
    "001_curso_MB/intermedio/006_my_file.txt", "w+")  # leer y escribir o crear
txt_file.write("Mi nombre es Carlos\nMi apellido es Garcia\ntengo 36 año\nMi lenguaje preferido es Python")

txt_file = open("001_curso_MB/intermedio/006_my_file.txt", "r+")  # leer y escribir
# print(txt_file.read())  # leer el fichero
# print(txt_file.read(10))    # separa el contenido cada 10 caracteres
# print(txt_file.readline())  # imprimir una linea a la vez
# print(txt_file.readline())  # imprimir una linea a la vez

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAuque tambien me gusta javascript")  # agregamos un alinea al fichero

# crea el fichero


txt_file.close()
# os.remove('001_curso_MB/intermedio/006_my_file.txt') # elimina el fichero



