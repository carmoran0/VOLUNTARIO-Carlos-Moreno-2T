# He reutilizado el programa de clase que es super similar
def buclesss():
    elec = input("Tabla de multiplicar(1) o calculadora(2):")
    if elec == "1":
        nume = (int(input("Tabla del: ")))
        for cont in range(1, 10):
            print(cont, "x", nume, "=", cont * nume)
    if elec == "2":
        tipo = input("¿Quieres sumar(+), restar(-), multiplicar(*) o dividir(/)?:")
        if tipo == "+":
            cant = (int(input("Número de números: ")))
            suma = 0
            for cont in range(0, cant):
                num = (int(input("Numeros: ")))
                suma = suma + num
            print("=", suma)
        if tipo == "-":
            cant = (int(input("Número de números: ")))
            suma = (int(input("Numeros: ")))
            for cont in range(1, cant):
                num = (int(input("Numeros: ")))
                suma = suma - num
            print("=", suma)
        if tipo == "*":
            cant = (int(input("Número de números: ")))
            cant = cant + 1
            suma = 1
            for cont in range(1, cant):
                num = (int(input("Numeros: ")))
                suma = suma * num
            print("=", suma)
        if tipo == "/":
            cant = (int(input("Número de números: ")))
            suma = (int(input("Numeros: ")))
            for cont in range(1, cant):
                num = (int(input("Numeros: ")))
                suma = suma / num
            print("=", suma)
while True:
    buclesss()
