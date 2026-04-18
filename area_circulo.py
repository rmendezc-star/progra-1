import math
def area_circulo(radio):
    # calcula el area de un circulo
    # Args: radio (float)
    # Returns: area del circulo
    return math.pi * radio ** 2

def es_primo(n):
    # verifica si un número es primo
    # Args: n (int)
    # Returns: True o false
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def factorial(n):
    # calcula el factorial de un número
    # Args: n (int)
    # Returns: factorial de n
    if n < 0:
        return "no existe factorial de números negativos"
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado 