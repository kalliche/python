# Falto el profsor y los pibes van a armar la clase.

# pedir el nombre y la edad de los compañeros que vinieron hoya clase
# Función para obtener el asistente y al profesor egun la edad
def obtener_compañeros(contidad_de_compañeros):
    
    #Creando la lista de los compañeros
    compañeros = []
    
    # ejecotar un for para pedir información de cada compañero
    for i in range(contidad_de_compañeros):
        nombre = input('Ingresa el nombre del compañero -> ')
        edad = int(input('<ingresa la edad del compañero -> '))
        compañero = (nombre, edad)
        
        # agregando la información a la lista
        compañeros.append(compañero)
        
    # ordenarlos  de menos a marot segun su edad
    compañeros.sort(key=lambda x: x[1])
    
    # compañeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    # para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    # retorna un tupla
    return asistente, profesor

# desempaquetamos lo que nos retorna la función
asistente, profesor = obtener_compañeros(5)

# mostrando el resultado
print(f'El profesores: {profesor} y su asistente es {asistente}')
    
