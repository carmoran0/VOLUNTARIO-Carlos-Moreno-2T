palabra = input("polla: ")
lista = []
for letra in range(0,len(palabra)):
    lista.append(palabra[letra])
lista.reverse()
print(lista)
final = "0"
for i in lista:
    final = final + i
print(final)