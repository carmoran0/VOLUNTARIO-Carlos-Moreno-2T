
def ebaulador():
    print("------------------------")
    print("Calculador de notas EBAU")
    print("------------------------")
    # fase obligatoria
    notingles = float(input("Nota en ingles: "))
    notmates = float(input("Nota en mates: "))
    notlengua = float(input("Nota en lengua: "))
    nothisto = float(input("Nota en historia: "))
    if nothisto < 0 or notmates < 0 or notlengua < 0 or notingles < 0:
        print("No puedes tener nota negativa...")
        ebaulador()
    if nothisto > 10 or notmates > 10 or notlengua > 10 or notingles > 10:
        print("No puedes mas de 10...")
        ebaulador()
    notafaseobligatoria = (nothisto + notingles + notlengua + notmates)/4
    if notafaseobligatoria < 4:
        print("Tienes que sacar un mínimo de 4 puntos en la Fase Obligatoria para que pueda ponderar con bachillerato.")
        ebaulador()
    nmb = float(input("Nota media bachillerato: "))
    notacceso = nmb*0.6 + notafaseobligatoria*0.4
    if notacceso < 5:
        print("SUSPENSO")
        ebaulador()
    #fase voluntaria
    M1=float(input("Cuanto pondera tu voluntario 1? (0.1 o 0.2)(0 si no existe)"))
    nota=float(input("Cuanto has sacado en el voluntario 1?"))
    if nota > 10 or nota < 0:
        print("imposible")
    if nota < 5:
        print("Suspenso, no pondera")
        nota=0
    M2 = float(input("Cuanto pondera tu voluntario 2? (0.1 o 0.2)(0 si no existe)"))
    notb=float(input("Cuanto has sacado en el voluntario 2?"))
    if notb > 10 or notb < 0:
        print("imposible")
    if notb < 5:
        print("Suspenso, no pondera")
        notb=0
    if M1 != 0.2 and M1 != 0.1 and M1 != 0:
        print("Ponderacion invalida.")
        ebaulador()
    if M2 != 0.2 and M2 != 0.1 and 2 != 0:
        print("Ponderacion invalida.")
        ebaulador()
    notadmision =notacceso + nota *M1 + notb*M2
    print("Tu nota de admision es",notadmision)

ebaulador()
