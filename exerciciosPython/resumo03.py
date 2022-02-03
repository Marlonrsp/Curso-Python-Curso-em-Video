# exercício de quebrar um número

from math import trunc
n = float(input('Digite um número: '))
print('O número digitado foi {} e seu valor real é {} '.format(n, trunc(n)))

# exercício de catetos e hipotenusa

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjecente: '))
hi = hypot(co,ca)
print('A medida da hipotenusa é {:.2f} '.format(hi))

# exercício de seno, cosseno, tangente

from math import sin,cos,tan, radians
an = float(input('Digite o valor do angulo: '))
s = sin(radians(an))
print('O ângulo {} tem o Seno de: {:.2f}'.format(an,s))
c = cos(radians(an))
print('O ângulo {} tem o Cosseno de: {:.2f} '.format(an,c))
t = tan(radians(an))
print('O ângulo {} tem o Tangente de: {:.2f}'.format(an,t))

# exercício de sortear um item dentro da lista

from random import choice
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
lista = [n1,n2,n3]
escolhido = choice(lista)
print('O número escolhido foi o {} '.format(escolhido))

# exercício de sortear a ordem da lista

from random import shuffle
nm1 = str(input('Digite o nome do primeiro aluno: '))
nm2 = str(input('Digite o nome do segundo aluno: '))
nm3 = str(input('Digite o nome do teceiro aluno: '))
nm4 = str(input('Digite o nome do quarto aluno: '))
lista = [nm1,nm2,nm3,nm4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

# exercício de tocar MP3 com Python

# Obs: 
# Este exercício não pude concluir, pois no vscode não reconhece outras bibliotecas 
# fora as padrões do python como "pygame" utilizada pelo professor Gustavo Guanabara no vídeo do exercício 21
# do Curso em Vídeo. 
# Como funcionaria no Pycharm, não pude instalá-lo em minha máquina, pois este só reconhece em SO de 64 bit
# pois minha máquina está com um SO de 32 bit; retornarei a este exercício quando atualizar minha máquina.
 
