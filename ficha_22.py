# 22. Escriba una función que reciba una lista de 5 palabras y devuelva la que contenga más veces la letra a
def main():
    palabras = str(input("Escribe las palabras que quieras separadas por comas: "))
    listapa  = palabras.split(",")
    cuenta = []
    for worf in listapa:
        aas = 0
        for letra in range(0, len(worf)):
            letra = worf[letra]
            if (letra.casefold() == 'a'):
                print (letra, "es A")
                aas = aas + 1
        cuenta.append(aas)
    print(cuenta)
    valomax = max(cuenta)
    print(valomax)
    posfinal = cuenta.index(valomax)
    print(posfinal)
    print("LA PALABRA ES ", listapa[posfinal])

while True:
    main()