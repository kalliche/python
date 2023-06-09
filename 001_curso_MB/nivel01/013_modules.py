# modules
# para importar un modulo este debe estar renombrado sin mumeros formas nulas (010_variables) forma correcta variables

import module
module.sum_value(4,3,2)
module.print_value('Carlos el mejor programador')

from module import sum_value, print_value
sum_value(5, 6, 7)
print_value('Soy el mejor')

import math
print(math.pi)
print(math.pow(2, 8))