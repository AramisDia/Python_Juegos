import random

# Función para el juego "Adivina el número"
def adivina_numero():
    numero_aleatorio = random.randint(1, 10)
    intentos = 3

    print("----------------------------------------------------------------")
    print("¡Bienvenido a adivina el número!")
    print("Tienes 3 intentos para adivinar un número entre 1 y 10.")
    print("Escribe 'salir' en cualquier momento para abandonar el juego.")

    while intentos > 0:
        intento = input("Introduce tu número: ")
        
        if intento.lower() == 'salir':
            print("Has salido del juego.")
            return

        try:
            intento = int(intento)
            if intento < 1 or intento > 10:
                print("Por favor, introduce un número entre 1 y 10.")
                continue

            if intento == numero_aleatorio:
                print("¡Felicidades! Has adivinado el número.")
                return
            elif intento < numero_aleatorio:
                print("El número es mayor.")
            else:
                print("El número es menor.")
            
            intentos -= 1
            print(f"Te quedan {intentos} intentos.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")
    
    print(f"Has perdido. El número era {numero_aleatorio}.")

# Función para el juego "Piedra, Papel o Tijeras"
def piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    puntos_usuario = 0
    puntos_computadora = 0

    def determinar_ganador(jugador, computadora):
        if jugador == computadora:
            return "Empate"
        elif (jugador == "piedra" and computadora == "tijeras") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijeras" and computadora == "papel"):
            return "Jugador"
        else:
            return "Computadora"

    print("----------------------------------------------------------------")
    print("¡Bienvenido a Piedra, Papel o Tijeras!")
    print("El primero en llegar a 3 puntos gana.")
    print("Escribe 'salir' en cualquier momento para abandonar el juego.")

    while puntos_usuario < 3 and puntos_computadora < 3:
        jugador = input("Elige: piedra, papel o tijeras: ").lower()

        if jugador == 'salir':
            print("Has salido del juego.")
            return

        if jugador not in opciones:
            print("Opción inválida. Elige entre piedra, papel o tijeras.")
            continue

        computadora = random.choice(opciones)
        print("")
        print(f"La computadora eligió: {computadora}")

        ganador = determinar_ganador(jugador, computadora)

        if ganador == "Jugador":
            puntos_usuario += 1
            print(f"¡Ganaste esta ronda! Puntos: Jugador {puntos_usuario} - Computadora {puntos_computadora}")
        elif ganador == "Computadora":
            puntos_computadora += 1
            print(f"Perdiste esta ronda. Puntos: Jugador {puntos_usuario} - Computadora {puntos_computadora}")
        else:
            print("Empate, nadie gana puntos.")

    if puntos_usuario == 3:
        print("¡Felicidades! Ganaste el juego.")
    else:
        print("La computadora ganó el juego.")

# Función para cargar palabras desde un archivo
def cargar_palabras():
    try:
        with open("palabras.txt", "r", encoding="utf-8") as archivo:
            palabras = [linea.strip() for linea in archivo if 3 <= len(linea.strip()) <= 7]
            return palabras if palabras else ["python", "java", "html"]
    except FileNotFoundError:
        print("No se encontró el archivo 'palabras.txt'. Se usará una lista por defecto.")
        return ["python", "java", "html", "css", "php", "hola", "adios", "raton", "casa"]

# Función para el juego "El Ahorcado"
def el_ahorcado():
    palabras = cargar_palabras()
    palabra_seleccionada = random.choice(palabras)
    intentos = len(palabra_seleccionada) * 2
    letras_adivinadas = ["_"] * len(palabra_seleccionada)
    letras_usadas = []

    # Mostrar la primera letra
    primera_letra = palabra_seleccionada[0]
    letras_adivinadas[0] = primera_letra

    print("----------------------------------------------------------------")
    print("¡Bienvenido a El Ahorcado!")
    print(f"La palabra tiene {len(palabra_seleccionada)} letras. Tienes {intentos} intentos para adivinarla.")
    print(f"Ya tienes una pista, la primera letra es: {primera_letra.upper()}")
    print("Escribe 'salir' en cualquier momento para abandonar el juego.")

    while intentos > 0 and "_" in letras_adivinadas:
        print("Palabra:", " ".join(letras_adivinadas))
        letra = input("Introduce una letra: ").lower()

        if letra == 'salir':
            print("Has salido del juego.")
            return

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Por favor, introduce una letra.")
            continue

        if letra in letras_usadas:
            print("Ya has usado esa letra. Intenta con otra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra_seleccionada:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            for i, l in enumerate(palabra_seleccionada):
                if l == letra:
                    letras_adivinadas[i] = letra
        else:
            intentos -= 1
            print(f"La letra '{letra}' no está en la palabra. Te quedan {intentos} intentos.")
    
    if "_" not in letras_adivinadas:
        print(f"¡Felicidades! Has adivinado la palabra: {palabra_seleccionada}")
    else:
        print(f"Has perdido. La palabra era: {palabra_seleccionada}")


# Menú principal para seleccionar el juego
def menu():
    while True:
        print("\n    Menú Principal    \n")
        print("1-->Adivina el número")
        print("2-->Piedra, Papel o Tijeras")
        print("3-->El Ahorcado")
        print("4-->Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            adivina_numero()
        elif opcion == "2":
            piedra_papel_tijeras()
        elif opcion == "3":
            el_ahorcado()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

# Ejecutar el menú principal
menu()
