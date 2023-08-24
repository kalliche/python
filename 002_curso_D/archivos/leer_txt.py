archivo_sin_leer = open('texto_plano.txt', encoding='UTF-8')

# leer archivo completo
#archivo = archivo_sin_leer.read()

# leer linea por linea
lineas = archivo_sin_leer.readlines() # para leer una linea el metodo readline()
print(lineas)

# cerrar el archivo
archivo_sin_leer.close()