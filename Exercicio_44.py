import math as m 

num = int (input('\n Entre com o logaritmando:'))
base = int (input('\n Entre com a base: '))
logaritmo = m.log (num) / m.log (base)
print(f'\n  O logaritmo de {num} na base {base} é {logaritmo:.2f}')
print('\n')