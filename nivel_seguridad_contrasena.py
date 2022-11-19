def esvoc(letra):
    respuesta = False
    if (letra.casefold() == 'a' or letra == 'e' or letra == 'i' or letra
            == 'o' or letra == 'u'):
        respuesta = True
    return respuesta


def escon(letra):
    respuesta = False
    letra = letra.casefold()
    if letra.isalpha():
        if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
            respuesta = True
    return respuesta


def esnum(letra):
    respuesta = False
    if letra.isnumeric():
        respuesta = True
    return respuesta


def essymb(letra):
    respuesta = False
    if letra.isalnum():
        return respuesta
    else:
        respuesta = True
        return respuesta


def contrasen():
    fortal = 0
    print("---------------------")
    print("FORTALEZA CONTRASEÑAS")
    print("---------------------")
    password = input("Introduce tu contraseña: ")
    cuentavocales = 0
    cuentaconsonantes = 0
    cuentanums = 0
    cuentasymbs = 0
    for cont in range(0, len(password)):
        if esvoc(password[cont]):
            cuentavocales = cuentavocales + 1
        if escon(password[cont]):
            cuentaconsonantes = cuentaconsonantes + 1
        if esnum(password[cont]):
            cuentanums = cuentanums + 1
        if essymb(password[cont]):
            cuentasymbs = cuentasymbs + 1
    print("Tiene", len(password), "caracteres")
    print(cuentavocales, "vocales")
    print(cuentaconsonantes, "consonantes")
    print(cuentanums, "numeros")
    print(cuentasymbs, "símbolos")

    fortal = fortal + len(password) / 2

    if len(password) < 8:
        print("NO cumple el criterio de más de 8 carácteres")
        fortal = fortal - 1
    else:
        print("CUMPLE con el criterio de más de 8 carácteres")
    
    if password.isalpha:
        if password.islower() or password.isupper():
            print("NO cumple el criterio de tener mayus y minus")
            mayusminus = False
        else:
            print("CUMPLE el criterio de tener mayus y minus")
            mayusminus = True
            fortal = fortal + 1

    if cuentanums <= 1:
        print("NO cumple el criterio de tener nums y letras")
        fortal = fortal - 2
        numsylet = False
    else:
        print("CUMPLE el criterio de tener nums y letras")
        numsylet = True
        fortal = fortal + 2
    if mayusminus and numsylet == True:
        fortal = fortal + 1

    if cuentasymbs >= 1:
        print("CUMPLE el criterio de tener símbolos")
        fortal = fortal + 2
    else:
        print("NO cumple el criterio de tener símbolos")
        fortal = fortal - 1

    print("Nivel de fortaleza", fortal)
    print("Un ordenador tardaría ", 2**fortal/2, "días en descifrarla")


while True:
    contrasen()
