# tabuada

tb = int(input('Digite um número e descubra a sua tabuada: '))
print('{}x{}={}'.format(tb,1,tb*1))
print('{}x{}={}'.format(tb,2,tb*2))
print('{}x{}={}'.format(tb,3,tb*3))
print('{}x{}={}'.format(tb,4,tb*4))
print('{}x{}={}'.format(tb,5,tb*5))
print('{}x{}={}'.format(tb,6,tb*6))
print('{}x{}={}'.format(tb,7,tb*7))
print('{}x{}={}'.format(tb,8,tb*8))
print('{}x{}={}'.format(tb,9,tb*9))
print('{}x{}={}'.format(tb,10,tb*10))

# conversor de moedas
real = float(input('Digite o valor que você possui em sua carteira: R$'))
dolar = real / 5.52
print('Com o valor de R$ {} que você possui, poderá comprar até US$ {:.2f} dolares, na cotação atual!'.format(real,dolar))

# pintar parede
largura = float (input('Digite a largura da sua parede: '))
altura = float (input('Digite a altura da sua parede: '))
area = largura * altura
print('A dimensão da sua parede é de {} x {} e a sua área é de {:.3f}m² !'.format(largura,altura,area))
tinta = area / 2
print('Então, para poder pintar esta parede você irá precisar de {}l de tinta !'.format(tinta))

# desconto de produto
valor = float(input('Digite o valor atual do produto: R$'))
dsct = valor - (valor * 15 / 100)
print('O valor atual do produto é de {}, e com a promoção de %15 de desconto o produto sairá no valor de {:.2f}'.format(valor,dsct))
