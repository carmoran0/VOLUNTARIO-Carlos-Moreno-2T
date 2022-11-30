# Escribir una función que devuelva el salario semanal de un trabajador en base a las horas trabajadas
# y el pago por hora trabajada. Las horas ordinarias 
# (40 primeras horas de trabajo) a 30 euros/hora
# horas siguientes a 1.5 veces el precio de la hora ordinaria

def trabah():
    horas = 0
    pagoporhora = int(input("¿Cuanto te pagan por hora? [0 si por defecto]: "))
    if pagoporhora == 0:
        pagoporhora = 30
    horas = int(input("¿Cuantas horas a la semana?: "))
    if horas > 40:
        hextra = horas - 40
        horas = horas - 40
    else:
        hextra=0
    salariosemanal = (horas*pagoporhora)+hextra*(pagoporhora*1.5)
    print("Ganas ", salariosemanal , "Euros a la semana")
    salariomensual = (salariosemanal/7)*30
    print(salariomensual , "Euros al mes")
    salarioanual = salariomensual*12
    print(salarioanual , "Euros al año")
    
    

trabah()