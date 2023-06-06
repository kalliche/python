'''encontrar numero faltante en una matriz'''
def find_missing_numbers(n):
    numbers = set(n)
    length = len(n)
    uotput =[]
    for i in range(1, n[-1]):
        if i not in numbers:
            uotput.append(i)
    return uotput

list_of_numbers = [1,2,3,5,6,7,8,9,10,11,13,14,16]
print(find_missing_numbers(list_of_numbers))