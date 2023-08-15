# creando una funcion simple
def saludar():
    print("Hola soy elmejor")
    
saludar()

#funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'reina'
    elif (sexo == 'hombre'):
        adjetivo = 'titan'
    else:
        adjetivo = 'amor'
    print(f'Hola {nombre}, mi {adjetivo} ¿como estas?')

saludar('Valeria','mujer')
saludar('Carlos','Hombre')
saludar('Ruth', 'no binario')

# crear una función que retorne valores
def crear_contraseña_random(num):
    chars = 'abcdefghijk'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}'
    #print(contraseña)
    return(contraseña)
password = crear_contraseña_random(83)
frase = f'Tu contraseña nueva es: {password}'
print(frase)