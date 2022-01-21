#Referente ao vídeo-aula 08 curso em vídeo

# Este primeiro exemplo pega toda as funções da biblioteca
# import math

# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print('A raiz quadrada do número {} é igual a {}'.format(num,math.ceil(raiz)))


# Este segundo exemplo pega somente aquilo que for necessario da biblioteca em questão

from math import sqrt

num = int(input('Digite um número para descobrir a sua raiz quadrada: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {}'.format(num,raiz))
