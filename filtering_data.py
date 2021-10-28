DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # Solamente los programadores de python

    # Solucion con list comprehensions

    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    # solucion con hig order functions

    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))


    # Solamente los trabajadores de platzi

    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    # Solucion con high order functions

    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))

    # Solamente los mayores de edad

    # Solucion con lsit comprehensions

    adults = [worker["name"] for worker in DATA if worker["age"] >= 18]

    # Solucion con hig order functions

    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))

    adults = list(map(lambda worker: worker["name"], adults))


    # Crear nueva lista de diccionarios que contenga una llave mas llavada old de valor booleana
    # True si la persona es mayor a 70 años y viceversa

    # Solucion con list comprehensions

    old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]

    # Solucion con hig order functions

    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    # la caracteristica de concatenar diccionarios con el simbolo pipe solo funciona
    # con versiones de python >= a python3.9

    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()