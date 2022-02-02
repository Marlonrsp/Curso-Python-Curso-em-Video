# Aleatório
import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1,n2,n3,n4] 
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

from random import shuffle
print('Bem vindo! Aqui professor, você ira fazer a ordem aleatória de apresentação dos alunos! ')
n1 = str(input('1º aluno: '))
n2 = str(input('2º aluno: '))
n3 = str(input('3º aluno: '))
n4 = str(input('4º aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será dos alunos: {}'.format(lista))