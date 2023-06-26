import json

json_file = open('001_curso_MB/intermedio/006_my_file.json', 'w+')    # leer y escribir o crear

json_test = {
    'name':'Carlos', 
    'surname':'Garcia', 
    'age':36, 
    'languages':["Python","Swift", "Kotlin"],
    'website':'https://carcode.com'
    }

# envioar la infoermación a json enviar información
json.dump(json_test, json_file, indent=0 )
json_file.close()

with open('001_curso_MB/intermedio/006_my_file.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open('001_curso_MB/intermedio/006_my_file.json'))
print(json_dict)
print(type(json_dict))
print(json_dict['languages'])