
def cuenta_atras(num):
    num -=1
    if num>0:
        print(num)
        cuenta_atras(num)
    else:
        print('Booooom!')
    print('Fin de la función')

if __name__=="__main__":
    print(5)
    cuenta_atras(5)