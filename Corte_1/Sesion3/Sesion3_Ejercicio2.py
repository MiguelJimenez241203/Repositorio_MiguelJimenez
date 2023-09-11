def costo_parqueo(tiempo_minutos,tarifa_tiempo):
    sin_iva=tiempo_minutos*tarifa_tiempo
    iva=sin_iva*0.19
    con_iva=sin_iva+iva
    redondeado=round(con_iva/50)*50
    return redondeado
tarifa_tiempo=139

try: 
    tiempo_minutos=int(input('Ingrese los minutos que estuvo parqueado: '))
    if tiempo_minutos<0:
        print('El tiempo de parqueo es imposible sea negativo ')
    else:
        costo_total=costo_parqueo(tiempo_minutos,tarifa_tiempo)
        print(f"Costo total del parqueo: ${costo_total:.2f}")
except ValueError:
    print('Algo pusiste mal ')

