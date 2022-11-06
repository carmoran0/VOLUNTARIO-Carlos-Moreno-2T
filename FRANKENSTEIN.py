import time
import random

FUERA = 'https://thumbs.dreamstime.com/b/usted-est%C3%A1-fuera-de-aqu%C3%AD-47910429.jpg'
bal = 0


def menu():
    global bal
    print ("Tienes", bal, "Antoniofichas™")
    quehacer = input("¿Quieres jugar ruleta (1), tragaperras (2), comprar fichas (3) o retirar ganancias (4)?")
    if quehacer == "1":
        print( )
        ruleta()
    if quehacer == "2":
        tragaperras()
        print( )
    if quehacer == "3":
        ingresar()
        print( )
    if quehacer == "4":
        retirar()
        print( )
    else:
        menu()
        print( )


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
        print("Bienvenido al Tragaperras Antonieto, 10AC la tirada")
        time.sleep(1)
        bal = int(input("¿Cuantas Antoniocoins™ desea depositar? (Debido a la inflacion, 1ac=0.0000456USD):"))
        time.sleep(1)
        tale = random.randint(3, 5)
        for cont in range(1, tale):
            print("Procesando.")
            time.sleep(0.5)
            print('\n' * 150)
            print("Procesando..")
            time.sleep(0.5)
            print('\n' * 150)
            print("Procesando...")
            time.sleep(0.5)
            print('\n' * 150)
        rea = input("¿Preparado? ^[Y/N]")
        if rea != "Y":
            quit()
        if rea == "Y":
            while True:
                if bal < 0:
                    print("Te quedaste sin AntonioCoins...")
                    bal = bal + 100
                    sn = input(
                        "Te gustaria un rescate de 100 AntonioCoins a cambio de un miembro de su familia (a elegir):[Y/N]")
                    if sn != "Y":
                        quit()
                print("Tienes ", bal, " AntonioCoins.")
                time.sleep(2)
                bal = bal - 10
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
                    cosa1 = "[Limon]"
                if cosanum2 == 6:
                    cosa2 = "[Naranja]"
                if cosanum2 == 7:
                    cosa2 = "[¡Diamante!]"
                cosanum3 = random.randint(1, 8)
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
                    print("Diamante, +10 AntonioCoins.")
                    bal = bal + 20

                if cosa2 == "[¡Diamante!]":
                    print("Diamante, +10 AntonioCoins.")
                    bal = bal + 20
                if cosa3 == "[¡Diamante!]":
                    print("Diamante, +10 AntonioCoins.")
                    bal = bal + 20
                if cosa1 == cosa2 == cosa3:
                    print("¡Ganaste 1000ac!")
                    bal = bal + 10
                    bal = bal + 10000
                    time.sleep(1)
                    sj = input("¿Te gustaría seguir jugando?[Y/N]")
                    if sj != "Y":
                        quit()
    else:
        print("No tienes suficientes fichas para jugar, por favor compra para jugar")
        time.sleep(2)
        menu()


def ruleta():
    global bal
    if bal > 0:
        print("----")
        print("Bienvenido a la ruleta")
        time.sleep(1)
        print("Antes de nada, la ruleta puede resultar muy adictiva y conlleva riesgo de")
        time.sleep(2)
        print("pérdidas de dinero, si no tiene problemas con las apuestas puede seguir jugando")
        time.sleep(2)
        print("y si los tiene...")
        time.sleep(2)
        print("pues juega también.")
        time.sleep(0.5)
        print("----")
        print("Ahora veamos las normas:")
        print("Si fallas perderás tu apuesta")
        print("Si aciertas duplicaras tu apuesta")
        print("Si aciertas apostando al CERO ganarás un 777%")
        print()
        print("El casino ha tenido la bondad de prestarle 100 Antoniocoins, aprovéchelos bien")
        time.sleep(1)
        a = 0
        bal = 100
        b = "nosecomovaesto"
        for cosa in b:
            print("----")
            time.sleep(1)
            print("Tienes esta cantidad de dinero ->", bal)
            time.sleep(1)

            apuesta = input("¿Apuestas a PAR, IMPAR o CERO? -->")
            cuanto = int(input("¿Cuanto dinero quieres apostar? -->"))
            if (0 >= bal):
                print("Nos debes pasta, vete a trabajar a las minas o algo, pero aquí no te queremos más")
                print("Fuera tío")
                time.sleep(5)
                print("TE HE DICHO QUE FUERA, ESTAMOS CERRADOS")
                time.sleep(3)
                print("PUM")
                break

            if (bal < cuanto):
                cuanto = 0
                print("Te falta dinero, lo siento")

            if (cuanto == bal):
                print("Así me gusta, con valentía")

            print("----")
            import random
            time.sleep(1)
            resultado = random.randint(0, 36)
            print("SALIÓ EL", resultado)

            if resultado == 0:
                FINAL = "CERO"
            if resultado % 2 == 0 and resultado != 0:
                FINAL = "PAR"
            if resultado % 2 != 0 and resultado != 0:
                FINAL = "IMPAR"
            time.sleep(1)
            print("Y EL", resultado, "ES", FINAL)
            print("----")
            time.sleep(2)

            if (apuesta == FINAL) and (apuesta == "PAR"):
                a = cuanto * 2
                print("HAS GANADO", int(a))
                bal += int(a)

            if (apuesta == FINAL) and (FINAL == "IMPAR"):
                a = cuanto * 2
                print("HAS GANADO", int(a))
                bal += int(a)

            if (apuesta == FINAL) and (FINAL == "CERO"):
                a = cuanto * 14
                print("JACKPOT!!", int(a))
                bal += int(a)

            if (apuesta != "PAR") and (apuesta != "IMPAR") and (apuesta != "CERO"):
                print("No se qué es {", apuesta, "}")

            if (apuesta != FINAL):
                a = cuanto
                print("HAS PERDIDO", int(a))
                bal -= int(a)
    else:
        print("No tienes suficientes fichas para jugar, por favor compra para jugar")
        time.sleep(2)
        menu()


def retirar():
    print("...")

print("¿Bienvenido al casino, quieres apostar tu alma en apuestas que solo te harán sentir un gran vacio en tu alma? [Y/N]")
time.sleep(1)
ENTRAR = input("-->")
if (ENTRAR == "Y"):
    menu()
if ENTRAR == "N":
    print("¿Entonces para qué vienes?")
    print(FUERA)
else:
    print("Te he pedido una respuesta de Y o N, por maleducado ya no te dejo entrar :(")
