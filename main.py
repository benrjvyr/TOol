
from herramientas import herramientas
from juegos import juegos
from utils import limpiar

while True:
    print('TOol by #')
    print('==Opciones==')
    print('(1) Herramientas')
    print('(2) Mini Juegos')
    print('(3) Salir')
    try:
        eleccion = int(input('Seleccione una opción: '))
        limpiar()
        if eleccion == 1:
            herramientas()
        elif eleccion == 2:
            juegos()
        elif eleccion == 3:
            print('¡Nos vemos!')
            input('Presione ENTER para salir')
            break
    except:
        print('¡Elección no válida! Intente de nuevo.')
        input('Presione ENTER para reintentar')
        limpiar()
