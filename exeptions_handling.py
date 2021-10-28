def divisors(num):
    if num < 0:
        raise ValueError("No se se admiten numeros negativos")
    divisors = [i for i in range(1, num + 1) if num % i == 0]

    return divisors

def run():
    try:
        num = int(input('Ingresa un numero: '))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    run()