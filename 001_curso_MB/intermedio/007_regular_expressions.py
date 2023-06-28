### regular expresiones
import re

# match
my_string = 'Esta es la leccion numero 7: Leccion llamada Expresiones regulares'
my_other_string = 'Esta no es la leccion número 6: Manejo de ficcheros'

match = re.match('Esta es la leccion', my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match('Esta no es la leccion', my_string, re.I)
#if not(match == None): # otra forma de comprobar el none
if match != None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])

print(re.match('Esta es la leccion', my_other_string))

# search
search = re.search('leccion', my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall
findall = re.findall('leccion', my_string, re.I)
print(findall)

# split
print(re.split(':', my_string)) # busca y divide la cadena

# sub solo tooma el; primer elemento encontrado
print(re.sub('Expresiones regulares', 'RegEx', my_string)) # cambia la palabra
print(re.sub('[l|L]eccion', 'LECCION', my_string)) # cambia la leccion asi empiece por mayuscula o minuscula

# patrones patterns
print('----------------------------\n')

pattern = r'[l|L]eccion'
print(re.findall(pattern, my_string))

pattern = r'[l|L]eccion|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[A-z]'
print(re.findall(pattern, my_string)) #  traer todas las tetras de la cadena

pattern = r'[0-9]'
print(re.findall(pattern, my_string)) # trae clos nuemro que hay en my_string
print(re.search(pattern, my_string)) # busca las posicion de donde esta el numero

pattern = r'[l].*'
print(re.findall(pattern, my_string))

print('----------------------------\n')
# validation for mail
email = 'riesgos@cootep.com.co'
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
print(re.findall(pattern, email))
print(re.search(pattern, email))
print(re.match(pattern, email))