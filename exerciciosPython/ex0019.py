#Escolha
#importação geral da classe random
import random
nome1 = str(input('Primeiro Aluno: '))
nome2 = str(input('Segundo Aluno: '))
nome3 = str(input('Terceiro Aluno: '))
nome4 = str(input('Quarto Aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolha = random.choice(lista)
print('O aluno escolhido foi: {} '.format(escolha))

#importação única do choice da classe random
from random import choice

n1 = str(input('Valor do dado: '))
n2 = str(input('Valor do dado: '))
n3 = str(input('Valor do dado: ')) 
lista = [n1,n2,n3]
escolher = choice(lista)
print('O dado sorteado foi {} '.format(escolher))

