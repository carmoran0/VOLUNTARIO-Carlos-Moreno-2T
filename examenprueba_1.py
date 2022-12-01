rawpalabras = input("Palabras separadas por comas:")
listapa = rawpalabras.split(",")
print("Las palabras son",listapa)
consolista = []
for palabra in listapa:
    if len(palabra) >= 10:
        print(palabra,",tiene más de 10")
    consonantes = 0
    for letrapos in range(0, len(palabra)):
        if palabra[letrapos] != "a" and palabra[letrapos] != "e" and palabra[letrapos] != "i" and palabra[letrapos] != "o" and palabra[letrapos] != "u":
            consonantes = consonantes+1
    consolista.append(consonantes)
print(consolista)