# Cifra un solo carácter
def cifrar_caracter(c, desplazamiento):
    if c.isalpha():  # solo letras
        if c.islower():
            base = ord('a')
        else:
            base = ord('A')
        
        # posición en el alfabeto (0-25)
        posicion = ord(c) - base
        
        # aplicar desplazamiento con efecto circular
        nueva_pos = (posicion + desplazamiento) % 26
        
        return chr(base + nueva_pos)
    else:
        return c  # no cambia si no es letra


# Cifra un mensaje completo
def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for c in mensaje:
        resultado += cifrar_caracter(c, desplazamiento)
    return resultado


# Descifra un mensaje (desplazamiento inverso)
def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)


# PRUEBAS
print(cifrar_mensaje("hola", 3))          # krod
print(cifrar_mensaje("Hola Mundo!", 5))  # Mtqf Rzsit!
print(descifrar_mensaje("krod", 3))      # hola