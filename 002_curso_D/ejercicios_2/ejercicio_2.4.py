primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))

print(primos_hasta(15))