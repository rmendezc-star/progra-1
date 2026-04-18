# Imprime la tabla del número n
def tabla(n):
    print(f"--- Tabla del {n} ---")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()  # espacio


# Verifica si un número es primo
def es_primo(n):
    if n < 2:
        return False
    
    # solo hasta la raíz cuadrada
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


# Imprime tablas solo de números primos
def tablas_primos(limite):
    for num in range(2, limite + 1):
        if es_primo(num):
            tabla(num)


# PRUEBA
tablas_primos(10)