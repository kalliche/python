## exception handling (manejo de errores)
numbre_one = 5
number_two = 1
#number_two = '1'

# try except
try:
    print(numbre_one + number_two)
    print('No se ha producido un error')
except:
    # Se ejecuta si se produce una excepción
    print('Se ha producido un error')

# try except else finally
try:
    print(numbre_one + number_two)
    print('No se ha producido un error')
except:
    print('Se ha producido un error')
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print('La ejecucion continua correctamente')
finally:    # Opcional
    # se ejecuta siempre
    print('La ejecución continua')

# captura de tipo de exception
try:
    print(numbre_one + number_two)
    print('No se ha producido un error')
except ValueError as error:
    print(error)
except TypeError as error:
    print(error)
except Exception as error:
    print(error)