def pira():
    ha=int(input("¿Como de alta?: "))
    for cont in range(1,ha+1):
        print(" "*(ha-cont), "*"*cont*2)
pira()