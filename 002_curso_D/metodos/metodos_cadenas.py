'''
DIR -> devuelve la lista de atributos válidos del objeyo pasado

UPPER -> convierte a mayusculas
LOWER -> convierte  a minisculas
CAPITALIZE -> primera letra mayuscula

FIND -> método encuentra la primera aparición del valor especificado, sino devuelve 1
INDEX -> método encuentera la primera aparicion del valor especificado, sino devuelve una expreción 

ISNUMERIC -> si es numerico devuelve True
ISLPHA -> si es alpha numerico devuelve true

COUNT -> devuelve el numero de ocurrencias de una subcadena en cadena dada
LEN -> cuenta los caracteres de una cadena

ENDSWITH -> verifica si una cadena comienza con
STARTSWITH -> verifica si una cadena termina con

REPLACE -> remplaza un valor por otro
SPLIT -> separa por el parametro dado
'''

cadena1 = 'Hola soy Carlos'
cadena2 = 'Bienvenido maquinola'

# ************* METODOS QUE CAMBIAN EL VALOR ***********
mayuscula = cadena1.upper()
print(mayuscula)
minuscula = cadena1.lower()
print(minuscula)
tipo_oracion = cadena1.capitalize()
print(tipo_oracion)

# ************* METODOS QUE BUSCAN ***********
# FIND buscamos una cadena en otra cadena devuelve la posicion donde la encuentra sino hay concidencia devuelve -1
buscar_palabra = cadena1.find('soy')
print(buscar_palabra)

# INDEX igual que el find a direfencia que si no encuentra la referecia arraja un error
buscar_palabra1 = cadena1.index('r')
print(buscar_palabra1)

# ************* METODOS QUE CONSULTAN EL VALOR ***********
# si  es numerico devuelve true, si no false
es_numerico = cadena1.isnumeric()
print(es_numerico)
# si es lafanumerico devuelve true de lo contrario fslse, (alfanumerico solo acomprende las letras del abecedaria a - z)
es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

# ************* METODOS QUE CONTAR EL VALOR ***********
# cuenta las veces existe la (a) en la cadena
contar_coincidencias = cadena1.count('a')
print(contar_coincidencias)
#cuenta la logitud de la cadena
contar_coincidencias = len(cadena1)
print(contar_coincidencias)

# ************* METODOS QUE VERIFICAR SI EMPIEZA CON ESA LETRA ***********
empieza_con = cadena1.startswith('H')
print(empieza_con)
termina_con = cadena1.endswith('H')
print(termina_con)

# ************* METODOS QUE REEMPLAZAN ***********
cadena_nueva = cadena1.replace('Hola', 'Aloha')
print(cadena_nueva)