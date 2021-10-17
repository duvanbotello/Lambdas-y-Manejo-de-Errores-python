def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Ingresa un numero: '))
        assert num.isnumeric(), "Debes ingresar un numero"
        print(divisors(num))
        print("termina mi programa")
    except ValueError:
        print('Por favor ingrese un numero')


if __name__ == '__main__':
    run()