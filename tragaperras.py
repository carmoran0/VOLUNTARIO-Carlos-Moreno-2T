# Por Carlos :)
import time
import random
def Tragaperras():
    print("Bienvenido al Tragaperras Antonieto, 10AC la tirada")
    time.sleep(1)
    ac=int(input("¿Cuantas Antoniocoins™ desea depositar? (Debido a la inflacion, 1ac=0.0000456USD):"))
    time.sleep(1)
    Tale=random.randint(3, 5)
    for cont in range(1, Tale):
        print("Procesando.")
        time.sleep(0.5)
        print('\n' * 150)
        print("Procesando..")
        time.sleep(0.5)
        print('\n' * 150)
        print("Procesando...")
        time.sleep(0.5)
        print('\n' * 150)
    rea=input("¿Preparado? ^[Y/N]")
    if rea != "Y":
        quit()
    if rea == "Y":
        while True:
            if ac < 0:
                print("Te quedaste sin AntonioCoins...")
                ac=ac+100
                sn=input("Te gustaria un rescate de 100 AntonioCoins a cambio de un miembro de su familia (a elegir):[Y/N]")
                if sn != "Y":
                    quit()
            print("Tienes ",ac," AntonioCoins.")
            time.sleep(2)
            ac=ac-10
            cosanum1=random.randint(1,7)
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
            cosanum2=random.randint(1,7)
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
            cosanum3=random.randint(1,8)
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
            print(cosa1,cosa2,cosa3)
            time.sleep(1)
            if cosa1 == "[¡Diamante!]":
                print("Diamante, +10 AntonioCoins.")
                ac=ac+20
                
            if cosa2 == "[¡Diamante!]":
                print("Diamante, +10 AntonioCoins.")
                ac=ac+20
            if cosa3 == "[¡Diamante!]":
                print("Diamante, +10 AntonioCoins.")
                ac=ac+20
            if cosa1 == cosa2 == cosa3:
                print("¡Ganaste 1000ac!")
                ac=ac+10
                ac=ac+10000
                time.sleep(1)
                sj=input("¿Te gustaría seguir jugando?[Y/N]")
                if sj != "Y":
                
                    quit()

while True:
    Tragaperras()
