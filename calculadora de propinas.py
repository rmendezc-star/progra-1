# Funciones base

def calcular_propina(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)


def calcular_total(subtotal, propina):
    return subtotal + propina


def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: número de personas inválido"
    return total / personas


def aplicar_descuento(subtotal, descuento_pct):
    return subtotal - (subtotal * (descuento_pct / 100))


# Menú
def mostrar_menu():
    print("\n--- CALCULADORA DE PROPINAS ---")
    print("1. Calcular propina")
    print("2. Dividir la cuenta")
    print("3. Aplicar descuento + propina")
    print("4. Salir")


# Función principal
def main():
    while True:
        mostrar_menu()
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            try:
                subtotal = float(input("Subtotal: Q"))
                print("Sugerencias: 10%, 15%, 20%")
                porcentaje = float(input("Porcentaje de propina: "))
                
                propina = calcular_propina(subtotal, porcentaje)
                total = calcular_total(subtotal, propina)
                
                print(f"Propina: Q{propina:.2f}")
                print(f"Total a pagar: Q{total:.2f}")
            except:
                print("Error: ingresa valores numéricos válidos")


        elif opcion == "2":
            try:
                total = float(input("Total de la cuenta: Q"))
                personas = int(input("Número de personas: "))
                
                resultado = dividir_cuenta(total, personas)
                
                if isinstance(resultado, str):
                    print(resultado)
                else:
                    print(f"Cada persona paga: Q{resultado:.2f}")
            except:
                print("Error: datos inválidos")


        elif opcion == "3":
            try:
                subtotal = float(input("Subtotal: Q"))
                descuento = float(input("Descuento (%): "))
                porcentaje = float(input("Propina (%): "))
                
                nuevo_subtotal = aplicar_descuento(subtotal, descuento)
                propina = calcular_propina(nuevo_subtotal, porcentaje)
                total = calcular_total(nuevo_subtotal, propina)
                
                print(f"Subtotal con descuento: Q{nuevo_subtotal:.2f}")
                print(f"Propina: Q{propina:.2f}")
                print(f"Total a pagar: Q{total:.2f}")
            except:
                print("Error: datos inválidos")


        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")


# Ejecutar
main()