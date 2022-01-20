dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foi rodado? '))
pagar = (dia * 60) + (km * 0.15)
print('O valor total a se pagar é de R${:.2f}'.format(pagar))
