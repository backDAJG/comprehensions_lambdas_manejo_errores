def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = { "firstname": "Alejandro", "lastname": "Jerez" }

    super_list = [
        { "firstname": "Alejandro", "lastname": "Jerez" },
        { "firstname": "Miguel", "lastname": "Torres" },
        { "firstname": "Pepe", "lastname": "Rodelo" },
        { "firstname": "Susana", "lastname": "Martinez" },
        { "firstname": "Jose", "lastname": "Garcia" },
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')

    for values in super_list:
        print(values)

if __name__ == '__main__':
    run()