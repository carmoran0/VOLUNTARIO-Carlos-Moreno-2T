def comprobacons(palabra):
    consonantes=0
    for cont in range(0,len(palabra)):
        if palabra[cont] != "a" and palabra[cont] != "e" and palabra[cont] != "i" and palabra[cont] != "o" and palabra[cont] != "u":
            consonantes=consonantes+1
    return consonantes

def main():
    first = ""
    palabra1=input("Palabra: ")
    print("Tiene ",comprobacons(palabra1)," consonantes")
    first = palabra1
    if len(palabra1) > 10:
        print("Es mayor que 10 caracteres")
    palabra2=input("Palabra: ")
    print("Tiene ",comprobacons(palabra2)," consonantes")
    if(comprobacons(palabra2)) > comprobacons(palabra1):
        first = palabra2
    if len(palabra2) > 10:
        print("Es mayor que 10 caracteres")
    palabra3=input("Palabra: ")
    print("Tiene ",comprobacons(palabra3)," consonantes")
    if(comprobacons(palabra3)) > comprobacons(palabra2):
        first = palabra3
    if len(palabra3) > 10:
        print("Es mayor que 10 caracteres")
    palabra4=input("Palabra: ")
    print("Tiene ",comprobacons(palabra4)," consonantes")
    if(comprobacons(palabra4)) > comprobacons(palabra3):
        first = palabra4
    if len(palabra4) > 10:
        print("Es mayor que 10 caracteres")
    palabra5=input("Palabra: ")
    print("Tiene ",comprobacons(palabra5)," consonantes")
    if(comprobacons(palabra5)) > comprobacons(palabra4):
        first = palabra5
    if len(palabra5) > 10:
        print("Es mayor que 10 caracteres")
    print("La palabra con más consonantes es: ",first)



main()
