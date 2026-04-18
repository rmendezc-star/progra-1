def calcular_billetes(monto):
    # Validar que sea múltiplo de 20
    if monto % 20 != 0:
        print("Error: el monto debe ser múltiplo de 20")
        return None

    # Calcular billetes
    b200 = monto // 200
    monto = monto % 200

    b100 = monto // 100
    monto = monto % 100

    b50 = monto // 50
    monto = monto % 50

    b20 = monto // 20

    # Mostrar resultado
    print(f"{b200}x Q200, {b100}x Q100, {b50}x Q50, {b20}x Q20")

    # Retornar valores (opcional)
    return (b200, b100, b50, b20)


# =========================
# PRUEBA DEL PROGRAMA
# =========================

monto = int(input("Ingrese el monto en quetzales: "))
calcular_billetes(monto)
