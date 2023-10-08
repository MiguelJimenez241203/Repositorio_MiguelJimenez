def database():
    data = 'wcm.csv'
    with open (data, "r", encoding="utf8") as archivo:
        next(archivo)
        mundiales = []
        for linea in archivo:
            linea = linea.rstrip('\n')
            lista = linea.split(",")
            home_team = lista[0]
            away_team = lista[1]
            home_score = int(lista[2])
            home_penalty = lista[3]
            away_score = int(lista[4])
            away_penalty = lista[5]
            home_manager = lista[6]
            home_captain = lista[7]
            away_manager = lista[8]
            away_captain = lista[9]
            attendance = int(lista[10])
            venue = lista[11]
            round = lista[12]
            date = lista[13]
            referee = lista[14]
            host = lista[15]
            year = lista[16]
            mundiales.append({
                'home_team': home_team,
                'away_team':away_team,
                'home_score':home_score,
                'home_penalty':home_penalty,
                'away_score':away_score,
                'away_penalty':away_penalty,
                'home_manager':home_manager,
                'home_captain':home_captain,
                'away_manager':away_manager,
                'away_captain':away_captain,
                'attendance':attendance,
                'venue':venue,
                'round':round,
                'date':date,
                'referee':referee,
                'host':host,
                'year':year,
            })
        return mundiales
    
def campeon_mundial():
    mundiales =  database()
    campeones = {}
    while True:
        print('''
            (1) Conocer cuantas veces fue campeón un país
            (2) Volver al programa principal 
            ''')
        respuesta = int(input('¿Qué opción va a elegir? '))
        if respuesta == 1:
            for partidos in mundiales:
                if partidos['round']=='Final':
                    if (partidos['home_score']>partidos['away_score'])or(partidos['home_penalty']>partidos['away_penalty']):
                        if partidos['away_team'] not in campeones:
                            campeones[partidos['away_team']]=[partidos['year']]
                        else:
                            list_year=campeones[partidos['away_team']]
                            list_year.append(partidos['year'])
                            campeones[partidos['away_team']]=list_year                
                    else:
                        if partidos['home_team'] not in campeones:
                            campeones[partidos['home_team']]=[partidos['year']]
                        else:
                            list_year=campeones[partidos['home_team']]
                            list_year.append(partidos['year'])
                            campeones[partidos['home_team']]=list_year
            campeones = dict(sorted(campeones.items()))
            
            pais=input('Ingrese un pais: ')
            
            if pais in campeones:
                year=campeones[pais]
                print(f'Fue campeon en los años {year}')
            else:
                print(f'{pais} no ha sido campeon del mundo')
        if respuesta == 2:
            print("Volviendo al programa principal...")
            break

def subcampeon_mundial():
    mundiales = database()
    subcampeones = {}
    while True:
        print('''
            (1) Conocer todos los subcampeones de los mundiales
            (2) Volver al programa principal 
            ''')
        respuesta = int(input('¿Qué opción va a elegir? '))
        if respuesta == 1:
            for partidos in mundiales:
                if partidos['round']=='Final':
                    if (partidos['home_score']>partidos['away_score'])or(partidos['home_penalty']>partidos['away_penalty']):
                        if partidos['away_team'] not in subcampeones:
                            subcampeones[partidos['away_team']]=[partidos['year']]
                        else:
                            list_year=subcampeones[partidos['away_team']]
                            list_year.append(partidos['year'])
                            subcampeones[partidos['away_team']]=list_year                
                    else:
                        if partidos['home_team'] not in subcampeones:
                            subcampeones[partidos['home_team']]=[partidos['year']]
                        else:
                            list_year=subcampeones[partidos['home_team']]
                            list_year.append(partidos['year'])
                            subcampeones[partidos['home_team']]=list_year
            print(subcampeones)
        if respuesta == 2:
            print("Volviendo al programa principal...")
            break
                   
def mayores_goleadas():
    mundiales = database()
    mayores_goleadas = []
    while True:
        print('''
            (1) Ver la lista completa de goles por mundial
            (2) Busqueda por mundial
            (3) Volver al programa principal
            ''')
        respuesta = int(input('¿Qué opción va a elegir? '))
        if respuesta == 1:
            for partidos in mundiales:
                resultado = abs(partidos['home_score']-partidos['away_score'])
                if resultado >=4:
                    mayores_goleadas.append({
                        'home_team': partidos['home_team'],
                        'away_team': partidos['away_team'],
                        'home_score': partidos['home_score'],
                        'away_score': partidos['away_score'],
                        'round': partidos['round'],
                    })
            for partidos in mayores_goleadas:
                resultado = abs(partidos["home_score"] - partidos["away_score"])
                print(f'Por {resultado} goles: {partidos["home_team"]} | {partidos["home_score"]} vs {partidos["away_score"]} | {partidos["away_team"]} (Ronda: {partidos["round"]})')
        if respuesta == 2:
            year = int(input('Escriba el año del mundial que desea consultar: '))
            for partidos in mundiales:
                resultado = abs(partidos['home_score']-partidos['away_score'])
                if resultado >=4 and int(partidos['year']) == year:
                    mayores_goleadas.append({
                        'home_team': partidos['home_team'],
                        'away_team': partidos['away_team'],
                        'home_score': partidos['home_score'],
                        'away_score': partidos['away_score'],
                        'round': partidos['round'],
                    })
            for partidos in mayores_goleadas:
                cantidad = int(input('Hasta cuantos partidos desea conocer (Maximo 10 y dele a 0 para salir del ciclo): '))
                if cantidad >=1:
                    cantidad = min(cantidad, len(mayores_goleadas))
                    for i in range(cantidad):
                        resultado = abs(mayores_goleadas[i]["home_score"] - mayores_goleadas[i]["away_score"])
                        print(f'Por {resultado} goles: {mayores_goleadas[i]["home_team"]} | {mayores_goleadas[i]["home_score"]} vs {mayores_goleadas[i]["away_score"]} | {mayores_goleadas[i]["away_team"]} (Ronda: {mayores_goleadas[i]["round"]})')
                elif cantidad == 0:
                    break

        elif respuesta == 3:
            print('Volviendo al programa principal...')
            break
                             
def enfrentamientos():
    mundiales = database()
    while True:
        print('''
            (1) Realizar la busqueda por país
            (2) Volver al programa principal
            ''')
        respuesta = int(input('¿Qué opción va a elegir? '))
        if respuesta == 1:
            pais1 = input('Digite el primer país a buscar: ')
            pais2 = input('Digite el segundo país a buscar: ')
            enfrentamientos = []
            enfrentamientos_conteo = 0  
            for partidos in mundiales:
                if (partidos['home_team'] == pais1 and partidos['away_team'] == pais2) or (partidos['home_team'] == pais2 and partidos['away_team'] == pais1):
                    enfrentamientos_conteo += 1
                    enfrentamientos.append({
                        'year': partidos['year'],
                        'home_score': partidos['home_score'],
                        'away_score': partidos['away_score'],
                        'round': partidos['round'],
                        'home_team': partidos['home_team'],
                        'away_team': partidos['away_team'],
                        'score': f"{partidos['home_score']} - {partidos['away_score']}",
                        #'winner': pais1 if partidos['home_score'] > partidos['away_score'] else pais2,
                    })
            if enfrentamientos_conteo == 0:
                print('-------------------------------')
                print(f'{pais1} y {pais2} no se han enfrentado nunca en mundiales')
            else:
                print('-------------------------------')
                print(f'Cantidad de partidos: {enfrentamientos_conteo}')
                for enfrentamiento in enfrentamientos:
                    print('-------------------------------')
                    print(f'{enfrentamiento["home_team"]} | {enfrentamiento["home_score"]} vs {enfrentamiento["away_score"]} | {enfrentamiento["away_team"]} - Ronda {enfrentamiento["round"]} Año: {enfrentamiento["year"]}')
                
                #profe, por más que intente no pude hacer que diera el ganador correcto, dejo comentado lo que tenia programado para el ganador
                        
        elif respuesta == 2:
            print("Volviendo al programa principal...")
            break

def main():
    while True:
        print('''
            (1) Campeones de los mundiales
            (2) Subcampeones de los mundiales
            (3) Mayores goleadas en los mundiales
            (4) Enfrentamientos de equipos en mundiales
            (5) Cerrar el programa
            ''')
        opc=int(input('¿Qué programa va a ejecutar? '))
        if opc == 1:
            campeon_mundial()
        if opc == 2:
            subcampeon_mundial()
        if opc == 3:
            mayores_goleadas()
        if opc == 4:
            enfrentamientos()
        if opc == 5:
            print('Saliendo...')
            break
                                                     
if __name__=="__main__":
    print('Bienvenido al programa de todos los mundiales'.center(60,'-'))
    main()
