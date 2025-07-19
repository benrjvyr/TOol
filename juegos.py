
import random
from utils import limpiar

def juego_uno():
    while True:
        print('Bienvenido a "Adivina el Número"')
        print('Tendrás que adivinar un número del 1 al 105')
        print('(1) Fácil (15 intentos)')
        print('(2) Normal (10 intentos)')
        print('(3) Difícil (5 intentos)')
        dificultad = int(input('Elige una dificultad: '))
        if dificultad == 1:
            intentos_d = 15
        elif dificultad == 2:
            intentos_d = 10
        elif dificultad == 3:
            intentos_d = 5
        else:
            print('Opción inválida')
            continue

        input('Presiona ENTER para empezar')
        limpiar()
        numero = random.randint(1, 105)
        intentos = 0

        while True:
            try:
                numero_ingresado = int(input('Ingresa un número: '))
            except ValueError:
                print('Solo se permiten números.')
                continue

            intentos += 1

            if numero_ingresado == numero:
                limpiar()
                print('¡Has ganado!')
                break
            elif intentos == intentos_d:
                limpiar()
                print('¡Perdiste! El número era:', numero)
                break
            elif numero_ingresado > numero:
                print('Menos')
            else:
                print('Más')

        volver = input('¿Deseas volver a jugar? (si/no): ')
        if volver.lower() != 'si':
            break
        limpiar()

def juegos():
    while True:
        print('Bienvenido a los juegos')
        print('(1) Adivina el número')
        print('(4) Volver')
        try:
            eleccion = int(input('Seleccione una opción: '))
            limpiar()
            if eleccion == 1:
                juego_uno()
            elif eleccion == 4:
                break
        except:
            print('¡Elección no válida! Intente de nuevo.')
            input('Presione ENTER para reintentar')
            limpiar()
