# listas una con el nombre y otra con apellido
nombres = ['lucas', 'Matias', 'Simon', 'Pedro', 'Roberto']
apellidos = ['Dalto', 'Zing', 'Gimenes', 'Burbano', 'Delgado']

# registrar esta información en un TXT de forma óptima
with open('nombre_y_apellidos.txt','w') as arch:
    arch.writelines('los datos son:\n')
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n--------------\n')for n,a in zip(nombres, apellidos)]