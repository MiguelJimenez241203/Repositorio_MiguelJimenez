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
            home_score = lista[2]
            home_penalty = lista[3]
            away_score = lista[4]
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
    
def subcampeon_mundial():
    mundiales = database()
    subcampeones = {}
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
    subcampeones = dict(sorted(subcampeones.items()))
    for pais,year in subcampeones.items():
        print(f'{pais}: campeón en {year}')

def campeon_mundial():
    mundiales =  database()
    campeones = {}
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
        print(f'fue campeon en los años {year}')
    else:
        print(f'{pais} no ha sido campeon del mundo')


def main():
    #subcampeon_mundial()
    campeon_mundial()
                           
if __name__=="__main__":
    print('Mundiales de 1930 a 2022'.center(60,'-'))
    main()