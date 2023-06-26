# .csv file
import csv

scv_file = open('001_curso_MB/intermedio/006_my_file.csv', 'w+')

scv_writer = csv.writer(scv_file)
scv_writer.writerow(['name','surname','age','language','website'])
scv_writer.writerow(['Carlos','Garcia',35,'Python','https://carcode.com'])
scv_writer.writerow(['Reinaldo','',30,'Cobol',''])

scv_file.close()

# ,xlsx file
# import xlrd # se debe instalar el modulo

# .xml file
import xml
