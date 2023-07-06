# Definimos las variables de color
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = "\033[1;33m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = '\033[0m'


def cabecera():
    print(title)
    print(divider)


title = """

██╗    ██╗ █████╗ ███████╗████████╗███████╗██████╗ 
██║    ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║███████║███████╗   ██║   █████╗  ██████╔╝
██║███╗██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝██║  ██║███████║   ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                   
Calculadora de gastos personales        < afsh4ck >
"""

divider = """---------------------------------------------------
"""

cabecera()

while True:
    print(
        AMARILLO + "[*] Bienvenido a tu calculadora de gastos personales" + RESET)

    # Pedimos el ingreso del usuario
    ingreso = float(
        input(VERDE + "[*] Introduce tus ingresos mensuales: " + RESET))

    # Inicializamos las variables de gastos
    vivienda = 0
    transporte = 0
    alimentacion = 0
    agua = 0
    electricidad = 0
    internet = 0
    prestamos = 0
    deporte = 0
    entretenimiento = 0
    otros = 0

    # Pedimos los gastos del usuario por categoría
    vivienda = float(input(ROJO + "[*] Gastos en vivienda: " + RESET))
    transporte = float(input(ROJO + "[*] Gastos en transporte: " + RESET))
    alimentacion = float(input(ROJO + "[*] Gastos en alimentación: " + RESET))
    agua = float(input(ROJO + "[*] Gastos en agua: " + RESET))
    electricidad = float(input(ROJO + "[*] Gastos en electricidad: " + RESET))
    internet = float(input(ROJO + "[*] Gastos en internet: " + RESET))
    prestamos = float(input(ROJO + "[*] Gastos en préstamos: " + RESET))
    deporte = float(input(ROJO + "[*] Gastos en deporte: " + RESET))
    entretenimiento = float(
        input(ROJO + "[*] Gastos en entretenimiento: " + RESET))
    otros = float(input(ROJO + "[*] Otros gastos: " + RESET))

    # Calculamos el total de gastos y el balance
    total_gastos = vivienda + transporte + alimentacion + agua + \
        electricidad + internet + prestamos + deporte + entretenimiento + otros
    balance = ingreso - total_gastos

    # Mostramos el resultado al usuario
    print(VERDE + "[*] Ingresos: {:.2f}".format(ingreso))
    print(ROJO + "[*] Gastos:")
    print("  - Vivienda: {:.2f}".format(vivienda))
    print("  - Transporte: {:.2f}".format(transporte))
    print("  - Alimentación: {:.2f}".format(alimentacion))
    print("  - Agua: {:.2f}".format(agua))
    print("  - Electricidad: {:.2f}".format(electricidad))
    print("  - Internet: {:.2f}".format(internet))
    print("  - Préstamos: {:.2f}".format(prestamos))
    print("  - Deporte: {:.2f}".format(deporte))
    print("  - Entretenimiento: {:.2f}".format(entretenimiento))
    print("  - Otros: {:.2f}".format(otros))
    print(RESET + "[*] Total de gastos: {:.2f}".format(total_gastos))

    if balance < 0:
        # Si el balance es negativo, mostramos el mensaje en rojo
        mensaje_color = ROJO
        mensaje = "[*] ¡Cuidado! Estás gastando más de lo que ganas."
    else:
        # Si el balance es positivo, mostramos el mensaje en verde
        mensaje_color = VERDE
        mensaje = "[*] ¡Excelente! Ahorraste {:.2f} este mes.".format(balance)

    # Imprimimos el mensaje con el color correspondiente
    print(mensaje_color + "[*] Balance: {:.2f}".format(balance) + RESET)
    print(mensaje)

    # Pedimos al usuario si quiere volver a calcular los gastos o terminar la sesión
    respuesta = input(
        MAGENTA + "[*] ¿Quieres volver a calcular tus gastos? (s/n): " + RESET)
    if respuesta.lower() != 's':
        # Si la respuesta no es 's' (es decir, si el usuario no quiere volver a calcular los gastos), salimos del bucle
        break
