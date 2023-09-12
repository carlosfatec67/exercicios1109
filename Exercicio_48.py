import math as m 

sm = float(input('\n Entre com o Salário Minimo: '))
quantidade = float (input('\n Entre com a quantidade de quilowatt: '))
preço = sm / 700 
vp = preço * quantidade 
vd = vp * 0.9 
print (f'\n Preço do quilowatt: {preço}\n Valor a ser pago:{vp}\n Valor com desconto: {vd} ')
print('\n')