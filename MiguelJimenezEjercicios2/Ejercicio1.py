L=(input('Digite una letra del abecedario '))
if L in 'aeiou':
    print('Es una vocal ')
else:
    if L in 'bcdfghjklmnñpqrstvwxyz':
        print('Es una consonante ')
    else:
        print('El valor ingresado no es una letra del abecedario.')
