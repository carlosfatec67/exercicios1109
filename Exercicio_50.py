import math as m 

base = float (input('\n Digite a Base:'))
altura = float (input('\n Digite a altura:'))
perimetro = 2* (base + altura)
area = base * altura 
diagonal = m.sqrt(base**2 + altura** 2)
print('f\n Perimetro: {perimetro}')
print('f\n Àrea : {area}')
print('f\n Diagonal: {diagonal : .2 f } ')
print('\n')
