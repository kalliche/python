# creando una (tupla, lista)
datos_en_tupla = ('Carlos', 'Garcia', 100000)
datos_en_lista = ['Carlos', 'Garcia', 100000]

# desempaquetando
nombre, apellido, suscriptores = datos_en_lista
nombre, apellido, suscriptores = datos_en_tupla

# resultrado
print(nombre)
print(apellido)
print(suscriptores)