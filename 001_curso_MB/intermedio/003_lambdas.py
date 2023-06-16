### lambdas ###

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(4,6))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(4,6))

# funciones con lmbda
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value
print(sum_three_values(5)(6,4))

# mas funciones con lambda
