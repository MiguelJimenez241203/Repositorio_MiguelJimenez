class Estudiante:
    def __init__(self):
        self.nombre=None
        self.peso=None
        self.altura=None
        self.IMC=None
        self.salud=None


def main():
    
    Paciente=[]
    
    persona1=Estudiante()
    persona1.nombre='Miguel Jimenez'
    persona1.peso=58
    persona1.altura=float(165/100)
    masa1=float(persona1.peso)/(persona1.altura)**2
    if masa1 < 18.5:
        persona1.salud='Su peso esta por debajo de lo estandar, coma mas'
    elif masa1 >= 18.5 and masa1 <= 24.9:
        persona1.salud='Su peso es saludable, siga asi'
    elif masa1 >=25 and masa1 <= 29.9:
         persona1.salud='Tiene sobrepeso, haga ejercicio'
    elif masa1 >=30 and masa1 <= 34.9:
         persona1.salud='Tiene obesidad grado I'
    elif masa1 >=35 and masa1 <= 39.9:
         persona1.salud='Tiene obesidad grado II'
    else:
        persona1.salud='Tiene obesidad grado III'
    persona1.IMC=round(masa1,2)
    Paciente.append(persona1)


    persona2=Estudiante()
    persona2.nombre='Roxana Marin'
    persona2.peso=47
    persona2.altura=float(160/100)
    masa2=float(persona2.peso)/(persona2.altura)**2
    if masa2 < 18.5:
        persona2.salud='Su peso esta por debajo de lo estandar, coma mas'
    elif masa2 >= 18.5 and masa2 <= 24.9:
        persona2.salud='Su peso es saludable, siga asi'
    elif masa2 >=25 and masa2 <= 29.9:
         persona2.salud='Tiene sobrepeso, haga ejercicio'
    elif masa2 >=30 and masa2 <= 34.9:
         persona2.salud='Tiene obesidad grado I'
    elif masa2 >=35 and masa2 <= 39.9:
         persona2.salud='Tiene obesidad grado II'
    else:
        persona2.salud='Tiene obesidad grado III'
    persona2.IMC=round(masa2,2)
    Paciente.append(persona2)

    persona3=Estudiante()
    persona3.nombre='Gustavo Quintero'
    persona3.peso=52
    persona3.altura=float(170/100)
    masa3=float(persona3.peso)/(persona3.altura)**2
    if masa3 < 18.5:
        persona3.salud='Su peso esta por debajo de lo estandar, coma mas'
    elif masa3 >= 18.5 and masa3 <= 24.9:
        persona3.salud='Su peso es saludable, siga asi'
    elif masa3 >=25 and masa3 <= 29.9:
         persona3.salud='Tiene sobrepeso, haga ejercicio'
    elif masa3 >=30 and masa3 <= 34.9:
         persona3.salud='Tiene obesidad grado I'
    elif masa3 >=35 and masa3 <= 39.9:
         persona3.salud='Tiene obesidad grado II'
    else:
        persona3.salud='Tiene obesidad grado III'
    persona3.IMC=round(masa3,2)
    Paciente.append(persona3)

    persona4=Estudiante()
    persona4.nombre='Paola Clavijo'
    persona4.peso=75
    persona4.altura=float(150/100)
    masa4=float(persona4.peso)/(persona4.altura)**2
    if masa4 < 18.5:
        persona4.salud='Su peso esta por debajo de lo estandar, coma mas'
    elif masa4 >= 18.5 and masa4 <= 24.9:
        persona4.salud='Su peso es saludable, siga asi'
    elif masa4 >=25 and masa4 <= 29.9:
         persona4.salud='Tiene sobrepeso, haga ejercicio'
    elif masa4 >=30 and masa4 <= 34.9:
         persona4.salud='Tiene obesidad grado I'
    elif masa4 >=35 and masa4 <= 39.9:
         persona4.salud='Tiene obesidad grado II'
    else:
        persona4.salud='Tiene obesidad grado III'
    persona4.IMC=round(masa4,2)
    Paciente.append(persona4)

    
    print('Consulte su masa corporal y su salud'.center(60,'-'))
    for i in Paciente:
        print(f'Nombre: {i.nombre} \n\
        Peso:{i.peso}\n\
        Altura: {i.altura}\n\
        IMC: {i.IMC}\n\
        {i.salud} \n')
        
if __name__=="__main__":
    main()