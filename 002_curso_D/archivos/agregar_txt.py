with open('texto_plano.txt', 'a', encoding='UTF-8') as archivo:
    #Agregar el archivo'
    # agregar varias lineas
    for i in range(5):
        archivo.write(f'linea {i + 1} agregando \n')