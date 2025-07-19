
import requests
from datetime import datetime
import psutil
from utils import limpiar

def ip():
    response = requests.get("https://api.ipify.org")
    if response.status_code == 200:
        print(f"Tu IP pública es: {response.text}")
    else:
        print("No se pudo obtener la IP pública")
    input('Presione ENTER para salir')
    limpiar()

def fecha_y_hora():
    print('La fecha y hora actual es:')
    print(datetime.now())
    input('Presione ENTER para salir')
    limpiar()

def Hardware():
    print('Tu Hardware')
    print('==CPU==')
    print("CPU (núcleos físicos):", psutil.cpu_count(logical=False))
    print("CPU (núcleos lógicos):", psutil.cpu_count(logical=True))
    print("Uso de la CPU (%) por núcleo:", psutil.cpu_percent(interval=1, percpu=True))

    print('==RAM==')
    memory = psutil.virtual_memory()
    print("RAM total:", memory.total)
    print("RAM disponible:", memory.available)
    print("Uso de RAM (%):", memory.percent)

    print('==DISCO==')
    for part in psutil.disk_partitions():
        print(f"{part.device} - {part.mountpoint} ({part.fstype})")
    print('==USO DEL DISCO==')
    print("Uso en '/' (%):", psutil.disk_usage('/').percent)

    print('==RED==')
    net_io = psutil.net_io_counters()
    print("Bytes recibidos:", net_io.bytes_recv)
    print("Bytes enviados:", net_io.bytes_sent)

    input('Presione ENTER para salir')
    limpiar()

def herramientas():
    while True:
        print('==Bienvenido a las herramientas==')
        print('(1) Ip')
        print('(2) Fecha y Hora')
        print('(3) Tu Hardware')
        print('(4) Volver')
        try:
            eleccion = int(input('Seleccione una opción: '))
            limpiar()
            if eleccion == 1:
                ip()
            elif eleccion == 2:
                fecha_y_hora()
            elif eleccion == 3:
                Hardware()
            elif eleccion == 4:
                break
        except:
            print('¡Elección no válida! Intente de nuevo.')
            input('Presione ENTER para reintentar')
            limpiar()
