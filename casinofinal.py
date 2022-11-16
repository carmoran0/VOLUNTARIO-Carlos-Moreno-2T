import time
import random
import webbrowser

bal = 0


def menu():
    global bal
    print("Tienes", bal, "Antoniofichas™")
    print("¿Quieres jugar ruleta (1), tragaperras (2), comprar fichas (3) o retirar ganancias (4)?")
    quehacer = input("-->")
    if quehacer == "1":
        ruleta()
    if quehacer == "2":
        tragaperras()
    if quehacer == "3":
        ingresar()
    if quehacer == "4":
        retirar()
    else:
        menu()


def ingresar():
    global bal
    print("Bienvenido a la tienda de Antoniofichas™")
    time.sleep(1.5)
    print("AVISO: Debido a la inflación, ahora una Antonioficha™ es equivalente a 0.4 EUR, disculpe las molestias")
    print("¿Cuantos euros de depósito? (Mínimo de 10 EUR)")
    dineroreal = int(input("-->"))
    time.sleep(1)
    if dineroreal < 10:
        print("La cantidad mínima de compra debe ser 10 EUR")
    else:
        bal = dineroreal / 0.4
        menu()


def tragaperras():
    global bal
    if bal > 0:
        print("Tienes", bal, "Antoniofichas™")
        print("Bienvenido al Tragaperras Antonieto, hay tiradas de 5,25,50 y 200 Antoniofichas™ [0 para salir]")
        time.sleep(1)
        print("¿Cuantas Antoniofichas™ desea apostar?:")
        apuestraga = int(input("-->"))
        if apuestraga == 0:
            menu()
        if apuestraga != 5 and apuestraga != 25 and apuestraga != 50 and apuestraga != 200:
            print("No.")
            time.sleep(1.5)
            tragaperras()
        if apuestraga > bal:
            print("No tienes suficiente para esa apuesta")
        time.sleep(1)
        tale = random.randint(3, 5)
        for cont in range(1, tale):
            print("Procesando.")
            time.sleep(0.5)
            print('\n' * 50)
            print("Procesando..")
            time.sleep(0.5)
            print('\n' * 50)
            print("Procesando...")
            time.sleep(0.5)
            print('\n' * 50)
        bal = bal - apuestraga
        # Aqui no lo hice con diccionario pero hubiera sido mucho mas comodo
        cosanum1 = random.randint(1, 7)
        if cosanum1 == 1:
            cosa1 = "[Cereza]"
        if cosanum1 == 2:
            cosa1 = "[Plátano]"
        if cosanum1 == 3:
            cosa1 = "[Campana]"
        if cosanum1 == 4:
            cosa1 = "[Uvas]"
        if cosanum1 == 5:
            cosa1 = "[Limon]"
        if cosanum1 == 6:
            cosa1 = "[Naranja]"
        if cosanum1 == 7:
            cosa1 = "[¡Diamante!]"
        cosanum2 = random.randint(1, 7)
        if cosanum2 == 1:
            cosa2 = "[Cereza]"
        if cosanum2 == 2:
            cosa2 = "[Plátano]"
        if cosanum2 == 3:
            cosa2 = "[Campana]"
        if cosanum2 == 4:
            cosa2 = "[Uvas]"
        if cosanum2 == 5:
            cosa2 = "[Limon]"
        if cosanum2 == 6:
            cosa2 = "[Naranja]"
        if cosanum2 == 7:
            cosa2 = "[¡Diamante!]"
        cosanum3 = random.randint(1, 7)
        if cosanum3 == 1:
            cosa3 = "[Cereza]"
        if cosanum3 == 2:
            cosa3 = "[Plátano]"
        if cosanum3 == 3:
            cosa3 = "[Campana]"
        if cosanum3 == 4:
            cosa3 = "[Uvas]"
        if cosanum3 == 5:
            cosa3 = "[Limon]"
        if cosanum3 == 6:
            cosa3 = "[Naranja]"
        if cosanum3 == 7:
            cosa3 = "[¡Diamante!]"
        print(cosa1, cosa2, cosa3)
        time.sleep(1)
        if cosa1 == "[¡Diamante!]":
            print("Diamante, reembolso.")
            bal = bal + apuestraga
        if cosa2 == "[¡Diamante!]":
            print("Diamante, reembolso.")
            bal = bal + apuestraga
        if cosa3 == "[¡Diamante!]":
            print("Diamante, reembolso.")
            bal = bal + apuestraga
        if cosa1 == cosa2 == cosa3:
            print("¡Ganaste, multiplicas tu apuesta por 20!")
            bal = bal + apuestraga
            bal = apuestraga * 20
            time.sleep(1)
        tragaperras()
    else:
        print("No tienes suficientes fichas para jugar, por favor compra para jugar")
        time.sleep(2)
        menu()


def ruleta():
    global bal
    if bal > 0:
        print("Bienvenido a la ruleta")
        time.sleep(1)
        print("Antes de nada, la ruleta puede resultar muy adictiva y conlleva riesgo de")
        time.sleep(1)
        print("pérdidas de dinero, si no tiene problemas con las apuestas puede seguir jugando")
        time.sleep(1)
        print("y si los tiene...")
        time.sleep(1)
        print("pues juega también.")
        time.sleep(0.5)
        print("----")
        print("Ahora veamos las normas:")
        print("Si fallas perderás tu apuesta")
        print("Si aciertas duplicaras tu apuesta")
        print("Si aciertas apostando al CERO ganarás un 777%")
        time.sleep(1)
        b = "nosecomovaesto"
        for cosa in b:
            print("----")
            time.sleep(1)
            print("Tienes", bal, "Antoniofichas™")
            time.sleep(1)
            apuesta = input("¿Apuestas a PAR, IMPAR o CERO? [X para salir]--> ")
            if apuesta == "X":
                menu()
            cuanto = int(input("¿Cuantas Antoniofichas™ quieres apostar? --> "))
            if bal < cuanto:
                cuanto = 0
                print("Te falta dinero, lo siento")
            if cuanto == bal:
                print("Así me gusta, con valentía")
            print("----")
            time.sleep(1)
            resultado = random.randint(0, 36)
            print("SALIÓ EL ", resultado)
            if resultado == 0:
                final = "CERO"
            if resultado % 2 == 0 and resultado != 0:
                final = "PAR"
            if resultado % 2 != 0 and resultado != 0:
                final = "IMPAR"
            time.sleep(1)
            print("Y EL", resultado, "ES", final)
            print("----")
            time.sleep(2)
            if (apuesta == final) and (apuesta == "PAR"):
                a = cuanto * 2
                print("HAS GANADO", int(a))
                bal += int(a)
            if (apuesta == final) and (final == "IMPAR"):
                a = cuanto * 2
                print("HAS GANADO", int(a))
                bal += int(a)
            if (apuesta == final) and (final == "CERO"):
                a = cuanto * 14
                print("JACKPOT!!", int(a))
                bal += int(a)
            if (apuesta != "PAR") and (apuesta != "IMPAR") and (apuesta != "CERO"):
                print("No se qué es {", apuesta, "}")
            if apuesta != final:
                a = cuanto
                print("HAS PERDIDO", int(a))
                bal -= int(a)
    else:
        print("No tienes suficientes fichas para jugar, por favor compra para jugar")
        time.sleep(2)
        menu()


def retirar():
    print("Bienvenido al complejo proceso de retirada de dinero.")
    time.sleep(.5)
    print("La cantidad mínima para retirar son 250 Antoniofichas™.")
    time.sleep(.5)
    print("¿Cuantas fichas deseas retirar? (1 ficha = 0,4EUR)")
    retiro = int(input("-->"))
    if retiro < 250:
        print("Necesarias más fichas para retirar")
        time.sleep(0.5)
        menu()
    else:
        time.sleep(0.5)
        print("Correctamente retirados ", retiro * 0.4, "EUR")
        menu()


print(
    "¿Bienvenido al casino, quieres apostar tu alma en apuestas que solo te harán sentir un gran vacio en tu alma? ["
    "Y/N]")
ENTRAR = input("-->")
if ENTRAR == "Y":
    menu()
if ENTRAR == "N":
    print("¿Entonces para qué vienes?")
    time.sleep(1.5)
    webbrowser.open('https://thumbs.dreamstime.com/b/usted-est%C3%A1-fuera-de-aqu%C3%AD-47910429.jpg')
else:
    print("Te he pedido una respuesta de Y o N, por maleducado ya no te dejo entrar :(")
