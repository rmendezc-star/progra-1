import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7

while intentos < max_intentos:
    adivinanza = int(input("Adivina "
    "(1-100):"))
    intentos += 1

    if adivinanza < numero_secreto:
        print("mas alto")
    elif adivinanza > numero_secreto:
        print("mas bajo")
        
    else:
        print(f"¡correcto en {intentos}intentos!")
        break

  





