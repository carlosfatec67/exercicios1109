import math as m 

a = int(input('\n Entre com a base: '))
b = int(input('\n Entre com a altura : '))
c = int(input('\n Entre com a profundidade : '))
diagonal = m.sqrt (a**2 + b**2 + c**2 )
print(f'\n Diagonal: {diagonal: . 2 f }')
print('\n')