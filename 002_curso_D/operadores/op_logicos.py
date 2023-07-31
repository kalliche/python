# AND
resultado = True & True     #Devuenve True
print(f' << True & True >>  {resultado}')
resultado1 = False & True     #Devuenve False
print(f' << False & Tru >>  {resultado1}')
resultado2 = True & False     #Devuenve False
print(f' << True & Fals >>  {resultado2}')
resultado3 = False & False     #Devuenve False
print(f' << False & Fal >>  {resultado3}')

# OR
resultado4 = True | True     #Devuenve True
print(f'\n<< True | True >> {resultado4}')
resultado5 = False | True     #Devuenve True
print(f'<< False | True >> {resultado5}')
resultado6 = True | False     #Devuenve True
print(f'<< True | False >> {resultado6}')
resultado7 = False | False     #Devuenve False
print(f'<< False | False >> {resultado7}')

# NOT
resultado8 = not True    #Devuenve False
print(f'\n << not True >> {resultado8}')
resultado9 = not False    #Devuenve True
print(f' << not False >> {resultado9}')