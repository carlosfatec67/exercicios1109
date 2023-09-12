import math as m 
lado = float ( input ('\n Digite o lado do quadrado: '))
perimetro = 4 * lado
area = lado **2 
diagonal = lado * m.sqrt (2)
print(f'\n Perimetro: {perimetro}')
print(f'\n Área : {area} ')
print(f'\n Diagonal: {diagonal : .2 f } ')
print('\n')