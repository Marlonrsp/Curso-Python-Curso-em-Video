#calcular desconto
vlp = float(input(' Qual é o valor desse produto? R$ '))
des = vlp - (vlp * 5 / 100)
print('O valor do produto é de {}, e com o descondo de 5% passa a ser de: {:.2f}'.format(vlp,des))
