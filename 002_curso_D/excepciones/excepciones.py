# retornas la suma de dos numeros (no string)
def sumar_dos():
    while True:
        # solicitar los dos numeros para operación
        a = input('numero 1: ')
        b = input('numero 2: ')
        try:
            resultado = int(a) + int(b)
            break
        except Exception as e:
        #except ValueError es e:  #regresa los valores del error
            # si lanza una excepcion, solicitar los numeros nuevamente
            print('Te pedi un numero, ingresanuevamente dos numeros')
            # mostramos el error
            print(f'Error: {e}')
        else:
            break
        finally:
            print('esto se ejecuta siempre')
    return resultado

print(sumar_dos())