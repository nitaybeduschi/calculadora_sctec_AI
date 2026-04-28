import math


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


def potencia(base, expoente):
    return base ** expoente


def raiz_quadrada(x):
    if x < 0:
        raise ValueError("NÃ£o Ã© possÃ­vel calcular raiz quadrada de nÃºmero negativo")
    return math.sqrt(x)


def fatorial(n):
    if n < 0:
        raise ValueError("Não é possível calcular fatorial de número negativo")
    if n == 0:
        return 1
    return n * fatorial(n - 1)


def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
