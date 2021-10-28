def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # list comprehensions [<element> for <element> in <iterable> <condition>]

    # <element>: Representa a cada uno de los elementos a poner en la nueva lista

    # for <element> in <iterable>: Ciclo a partir del cual se extraeran elementos
    # de otra lista o cualquier iterable

    # <condition>: Condicion opcional para filtrar los elementos del ciclo

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(squares)

if __name__ == '__main__':
    run()