### classes
class MyPerson:
    pass

print(MyPerson)
print(MyPerson())

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname =surname

my_person = Person('Carlos', 'Garcia')
print(f'{my_person.name} {my_person.surname}')

class MyPerson:
    def __init__(self, name, surname):
        self.full_name = f'{name} {surname}'

    def walk(self):
        print(f'{self.full_name} Esta caminando')

my_person = MyPerson('Reinaldo', 'Nastar')
print(my_person.full_name)
my_person.walk()
























