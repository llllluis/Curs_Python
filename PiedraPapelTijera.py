import random
nombre=input("Nombre?")
telefono=input("Telefono?")
def juego_piedra_papel_tijera():
    opciones = ['piedra', 'papel', 'tijera']  # Las opciones posibles
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    
    # Solicitar al jugador que elija
    while True:
        jugador = input("Elige: piedra, papel o tijera: ").lower()
        if jugador in opciones:
            break  # Si la opción es válida, salimos del bucle
        else:
            print("Opción no válida, por favor elige piedra, papel o tijera.")
    
    # La computadora elige aleatoriamente
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    
    # Determinamos quién gana
    if jugador == computadora:
        print("¡Es un empate!")
    elif (jugador == 'piedra' and computadora == 'tijera') or \
         (jugador == 'tijera' and computadora == 'papel') or \
         (jugador == 'papel' and computadora == 'piedra'):
        print("¡Ganaste! " + nombre)
    else:
        print("¡Perdiste! " + nombre)

# Iniciar el juego
juego_piedra_papel_tijera()
