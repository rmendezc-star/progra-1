
def tiene_mayuscula(texto):
    for c in texto:
        if c.isupper():
            return True
    return False

def tiene_digito(texto):
    for c in texto:
        if c.isdigit():
            return True
    return False

def tiene_especial(texto):
    especiales = "!@#$%"
    for c in texto:
        if c in especiales:
            return True
    return False

def validar_password(password):
    if len(password) < 8:
        return False
    if not tiene_mayuscula(password):
        return False
    if not tiene_digito(password):
        return False
    if not tiene_especial(password):
        return False
    return True

def diagnosticar_password(password):
    errores = []

    if len(password) < 8:
        errores.append("Debe tener al menos 8 caracteres")
    if not tiene_mayuscula(password):
        errores.append("Debe tener al menos una letra mayúscula")
    if not tiene_digito(password):
        errores.append("Debe tener al menos un dígito")
    if not tiene_especial(password):
        errores.append("Debe tener al menos un carácter especial (!, @, #, $, %)")

    if len(errores) == 0:
        print("La contraseña es válida")
    else:
        print("La contraseña NO es válida. Errores:")
        for e in errores:
            print("-", e)


# Ejemplo de uso
password = input("Ingrese una contraseña: ")

print(validar_password(password))
diagnosticar_password(password)