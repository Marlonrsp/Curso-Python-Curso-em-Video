# REINICIO DE TUDO EM PYTHON
# print('Olá Mundo!')
# print (7+4)   # este é a operação de soma  de dois numerais
# print ('7'+'4') # neste caso não é a soma de dois numerais e sim uma junção (python reconhece como união de palavras, e não como operação)

# CORRIGIDO CONFORME EXPLICAÇÃO
# print ('Olá' + 5) # neste caso não funcionaria corretamente pois o + estaria relacionado com a soma, porém como o numero 5 não esta em aspas, o python não reconhece dando erro pois não é soma nem junção de palavras
# print ('Olá' , 5) # neste caso reconheceria, pois não haveria erro em relação com o sinal de + devido a junção ou soma dos dois valores seja inteiro ou string

# CORRETO
# nome='Marlon'
# idade=23
# peso=123.5
# print(nome,idade,peso)

# CORRETO
# nome=input('Qual é o seu nome?')
# idade=input('Qual a sua idade?')
# peso=input('Quanto você pesa?')
#AULA REFERENTE AO VÍDEO 04 CURSO EM VÍDEO
# print(nome, idade, peso)

# DESAFIO 1 CORRETO
# nome=input('Qual é o seu nome?')
# idade=input('Qual é a sua idade?')
# peso=input('Quanto de massa corporal você pesa?')
# print('Olá ',nome,' seja muito bem vindo! É um prazer te conhecer !')
# print('Seja Bem Vindo ',nome,'a sua idade é de ', idade,' e seu peso corporal é de ',peso)

# DESAFIO 2 CORRETO 
# dia=input('Qual é o dia em que você nasceu?')
# mes=input('Em qual mês?')
# ano=input('No ano de:')
# print('Você nasceu no dia:',dia,' do mês', mes,' do ano de ',ano,'. Correto?')

# DESAFIO 3

num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
soma = num1 + num2
print ('A soma do primeiro número: ',num1,' mais o segundo número: ',num2,' resulta em: ',soma)
