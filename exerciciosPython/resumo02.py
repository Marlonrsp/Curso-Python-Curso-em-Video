# Tabuada
tb = int(input('Digite um número para saber sua tabuada: '))
print('{} x {} = {}'.format(tb,1,tb*1))
print('{} x {} = {}'.format(tb,2,tb*2))
print('{} x {} = {}'.format(tb,3,tb*3))


# conversor de moedas
real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 5.51 
print('Com o valor de {} R$ da sua carteira você pode comprar US$ {:.2f} dolares'.format(real,dolar))

# pintar parede
largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
area = largura * altura
print('A dimensão da sua parede é de {}x{} por {:.3f}m²'.format(largura,altura,area))
tinta = area / 2
print('A quantidade necessária para pintar a parede é de {}l de tinta'.format(tinta))

# calculo de desconto
preco = float(input('Digite o valor do produto: R$ '))
desconto = preco - (preco * 10 / 100)
print('O valor do produto era de {:.2f} R$ e com o desconto da promoção de 10% passa a ser de {:.2f}'.format(preco,desconto))
