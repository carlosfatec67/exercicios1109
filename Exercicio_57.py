import math as m 
pr1 = float(input('\n Digite pr1: '))
pr2 = float(input('\n Digite pr2: '))
mf = ( pr1 + pr2 ) /2 
print(f'\n Média truncada: {float(int((mf -0.5)+ 0.001))} ')
print(f'\n Média arrendondada: {float(int((mf +0.001)))} ')
print('\n')