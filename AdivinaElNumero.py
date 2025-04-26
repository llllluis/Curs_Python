import random

def adivina_el_numero():
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    numero_secreto = random.randint(1, 100)  # El número aleatorio entre 1 y 100
    intentos = 0
    
    while True:
        try:
            # El jugador ingresa un número
            jugador_numero = int(input("Adivina el número: "))
            intentos += 1
            
            # Comprobamos si el número ingresado es el correcto
            if jugador_numero < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif jugador_numero > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break  # Termina el juego cuando se adivina correctamente
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Llamamos a la función para iniciar el juego
adivina_el_numero()
