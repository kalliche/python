# String
my_string = 'Mi string'
my_oter_string = 'mi otra cadena'

print(len(my_string))
print(len(my_oter_string))

my_new_line_string = 'Este es un string\ncon salto de linea'
print(my_new_line_string)

my_new_line_string = '\tEste es un string con tabulación'
print(my_new_line_string)

my_new_line_string = 'Este es un string\ncon salto de linea'
print(my_new_line_string)

#formateo
name, surname, age = 'Carlos', 'Reinaldo', 37

print('Mi nombre es {} {} y mi edad es {}'.format(name,surname,age))
print('Mi nombre es %s %s y mi edad es %d' %(name,surname,age))
print(f'Mi nombre es {name} {surname} y mi edad es {age}')

# desempaquetado de caracteres
