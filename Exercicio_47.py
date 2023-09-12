import math as m 

num = int(input('\n Entre com um numero de 3 digitos : '))
c = num // 100 
d = num % 100 // 10 
u = num % 10 
num1 = u * 100 + d * 10 + c 
print(f'\n Numero: {num} ')
print(f'n Numero Invertido: {int (num1)}')
print('\n')