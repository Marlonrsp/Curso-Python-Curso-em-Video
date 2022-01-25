#reajuste salarial

salario = float(input('Digite o salario do funcionário: R$ '))
novo = salario + (salario * 15 / 100)
print('O salario do funcionário era de R$ {:.2f}; e com aumento de 15% passou a ser de R$ {:.2f} '.format(salario,novo))

#conversão de temperatura

c = int(input('Digite a temperatura atual em graus: °C'))
f = (c * 9/5) + 32
print('Esta é a temperatura de graus {} °C convertido para {} °F'.format(c,f))

#aluguel de carros

dia = int(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos km rodados com o carro?: '))
pagar = (dia * 50) + (km * 0.50) 
print('Você alugou o carro por {} dias e rodou {} km. O Total a pagar é: {:.2f}'.format(dia,km,pagar))
