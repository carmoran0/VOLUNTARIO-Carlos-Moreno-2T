# Escriba una función que reciba 3 números que representen una fecha (por ejemplo 3, 12, 2009) y
# muestre por pantalla la misma fecha en el formato 3 de Diciembre de 2009.
dia = int(input("DIA: "))
mes = int(input("MES: "))
ano = input("ANO: ")
meses = {1:"ENERO", 2:"febrero",3:"marzo", 4:"abril",5:"mayo", 6:"junio",7:"julio", 8:"agosto",9:"septiembre", 10:"octubre",11:"noviembre", 12:"DICIEMBRE NAVIDAD",}
print("ES  EL",dia, "de", meses[mes], "del ", ano)