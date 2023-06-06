# funciones

def my_function():
    print('Esto es una función')

my_function()
my_function()
my_function()

def sum_two_values(first_number,second_number):
    print(first_number + second_number)

sum_two_values(5,7)

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

# imprime none por que la funcion no retorna nada
my_result = sum_two_values(1.2, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10,5)
print(my_result)
print(sum_two_values_with_return(6,11))

# reordenar los valores de entrada
def print_name(name, surname):
    print(f'{name} {surname}')

print_name(surname='Garcia', name='Carlos')

# pasar varios parametros
def print_texts(*text):
    print(text)

print_texts('hola', 'Python', 'Caliche')

# imprime una lista  puede ser de una a varias
def print_text(*text):
    for text in text:
        print(text)

print_text('hola', 'Python', 'Caliche')