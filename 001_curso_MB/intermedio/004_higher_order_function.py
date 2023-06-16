### funciones de orden  superior ###

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5,2,sum_one))  # 8
print(sum_two_values_and_add_value(5,2,sum_five))   # 12

### closures ###

def sum_ten():
    def add(value):
        return value + 10
    return add
add_closure = sum_ten()
print(add_closure(5))
# profundizar

### built-in higher order function ###

numbers = [2,5,10,21,15]
print(f'\n{numbers}')
# map
def multiply_two(number):
    return number * 2
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# filter
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False
print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# reduce
 # opera un valor con el acomulado
from functools import reduce
def sum_two_values(first_value, second_value):
    return first_value + second_value
print(reduce(sum_two_values, numbers))