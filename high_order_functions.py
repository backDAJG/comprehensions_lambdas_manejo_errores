from functools import reduce

def run():
    #FILTER

    # filter: [1, 4, 5, 6, 13, 19, 21] => [1, 5, 13, 19, 21]

    # filter(<function>, <iterable>)

    my_list = [1, 4, 5, 6, 13, 19, 21]

    # Solucion con list comprehensions

    odd = [i for i in my_list if i % 2 != 0]

    print(odd)

    # Solucion con filter

    odd_lambda = list(filter(lambda x: x % 2 != 0, my_list))

    print(odd_lambda)

    # MAP

    # map: [1, 2, 3,4 , 5] => [1, 4, 9, 16, 25]

    # map(<function>, <iterable>)

    my_list = [1, 2, 3,4 , 5]

    # Solucion con list comprehencions

    odd = [i**2 for i in my_list]

    print(odd)

    # Solucion con map

    odd_lambda = list(map(lambda x: x**2, my_list))

    print(odd_lambda)

    # REDUCE

    # reduce: [2, 2, 2, 2, 2] => 32

    # es necesario importar reduce de functools

    # reduce(<function>, <iterable>)

    # la funcion de reduce recibe dos parametros donde a es el primero y b el que le sigue
    # dependiendo de la iteracion

    my_list = [2, 2, 2, 2, 2]

    all_mutiplied = 1

    # Solucion con for

    for i in my_list:
        all_mutiplied = all_mutiplied * i

    print(all_mutiplied)

    # Solucion con reduce

    all_mutiplied = reduce(lambda a, b: a* b, my_list)

    print(all_mutiplied)

if __name__ == '__main__':
    run()