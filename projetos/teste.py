from math import sqrt
a = float(input('Valor de a = '))
b = float(input('Valor de b = '))
c = float(input('Valor de c = '))
if a != 0 and b != 0 and c != 0:
    delta = (b ** 2) - (4 * a * c)
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (a * 2)
        x2 = (-b - sqrt(delta)) / (a * 2)
        print('As raízes são {} e {}.'.format(x1, x2))
    if delta == 0:
        x1 = (-b + sqrt(delta)) / (a * 2)
        print('A única raíz é {}'.format(x1))
    if delta < 0:
        print('A função não possui raíz.')
if a != 0 and b != 0 and c == 0:
    x1 = 0
    x2 = -b / a
    print('As raízes são {} e {}.'.format(x1, x2))
if a != 0 and b == 0 and c == 0:
    x2 = -sqrt(a)
    print('As raízes são {} e {}.'.format(x1, x2))
if a != 0 and b == 0 and c != 0:
    if c > 0 and a < 0:
        x1 = sqrt(c / -a)
        x2 = -sqrt(c / -a)
        print('As raízes são {} e {}.'.format(x1, x2))
    if c < 0 and a > 0:
        x1 = sqrt(-c / a)
        x2 = -sqrt(-c / a)
        print('As raízes são {} e {}.'.format(x1, x2))
    if c > 0 and a > 0 or c < 0 and a < 0:
        print('O sistema não tem raìzes.')
if a == 0 and b != 0 and c != 0:
    x1 = -(c / b)
    print('A raíz é {}.'.format(x1))
Xv = -b / (2 * a)
Yv = (a * Xv ** 2) + (b * Xv) + c
if a > 0:
    print('O ponto mínimo é ({},{})'.format(Xv, Yv))
if a < 0:
    print('O ponto máximo é ({},{}).'.format(Xv, Yv))