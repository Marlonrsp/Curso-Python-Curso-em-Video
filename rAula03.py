#Referênte a aula 07 do curso em vídeo "Operadores Aritiméticos"

#sinais de operações
# + = adição              exemplo 5+2 == 7
# - = subtração           exemplo 5-2 == 3
# * = multiplicação       exemplo 5*2 == 10 
# / = divisão             exemplo 5/2 == 2.5
# ** = potência           exemplo 5**2 == 25  "elevado à potência "ao quadrado"
# // = divisão inteira    exemplo 5//2 == 2   "resultado da divisão inteira sem números flutuantes ou números com vírgula"
# % = resto de divisão    exemplo 5%2 == 1    "resultante do restante da divisão inteira (ou seja, da divisão resultante de números flutuante)"

# Raiz Quadrada Exemplo 81**(1/2)

#ORDEM DE PRESCEDÊNCIA DOS OPERADORES
# 1º = () "parenteses" 
# 2º = ** "potência"
# 3º = * /  // % "multiplicação, divisão, divisão inteira e por fim o resto da divisão"
# 4º = + / "adição e subtração" 
# *********************************************************************

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
divI = n1 // n2
res = n1 % n2
rq = n1**(1/2)
rq2 = n2**(1/2)

# print('A soma resulta {}'.format(soma))
# print('A subtração resulta {}'.format(sub))
# print('A multiplicação resulta {}'.format(mult))
# print('A divisão resulta {:.3f}'.format(div)) #o :.3f se refere a quantas casa decimais eu quero que apareça na divisão
# print('A potenciação resulta {}'.format(pot))
# print('A divisão por inteiro resulta {}'.format(divI))
# print('O resto da divisão resulta {}'.format(res))
# # print('A raiz quadrada do primeiro valor é de {}'.format(rq))
# # print('A raiz quadrada do segundo valor é de {}'.format(rq2))

print('A soma resulta em: {0}\n A subtração resulta em: {1}\n A multiplicação resulta em: {2}\n A divisão resulta em: {3}\n A exponenciação resulta em: {4}\n A divisão por inteiro resulta em: {5}\n O resto da divisão resulta em: {6}\n A raiz quadrada do primeiro numero é de: {7}\n A raiz quadrada do segundo número é de: {8}'.format(soma, sub, mult, div,pot,divI, res,rq,rq2))








