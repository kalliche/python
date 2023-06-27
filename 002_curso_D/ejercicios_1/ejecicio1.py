# promedios
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_dalto = 1.5

# duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# diferencia de duracion
print('---------------------------')
print('El curso de Dalto dura')
diferencia_con_min = 100 - (curso_dalto / otros_cursos_min * 100)
print(f' - el curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')
diferencia_con_max = 100 - curso_dalto * 1000 // otros_cursos_max / 10
print(f' - el curso de dalto dura un {diferencia_con_max}% menos que el mas lento')
diferencia_con_promedio = 100 - (curso_dalto / otros_cursos_promedio * 100)
print(f' - el curso de dalto dura un {diferencia_con_promedio}% menos que el mas promedio')
print('---------------------------')

# calculando el porcentaje de duración removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
print(f'El crudo promedio eliminado')
tiempo_vacio_dalto = 100 - curso_dalto * 1000 // crudo_dalto / 10
print(f'este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')
print('---------------------------')

# mostrando la diferencia si los cursos durarn 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // curso_dalto / 10} horas de otros cursos ')
print(f'ver 10 horas de otros cursos equivale a ver {curso_dalto * 100 // otros_cursos_promedio/ 10} horas de este curso ')
print('---------------------------')