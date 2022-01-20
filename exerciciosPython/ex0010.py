# conversor de moedas
real = float(input('Quanto de dinheiro você possui? R$ '))
dolar = real / 5.51
euro = real / 6.28
print('Você possui R$ {:.2f} \n podendo comprar até US$ {:.2f} Dolares \n bem como poder comprar {:.2f} Euros !'.format(real,dolar,euro))
