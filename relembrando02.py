# média aritmética

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) /2
print('A média do aluno é de {}'.format(m))

# dobro, triplo, raiz quadrada
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O número prescrito foi {0}\n o dobro dele é de {1}\n seu triplo é {2}\n e a raiz quadrada é de {3}'.format(n,d,t,r))

# conversor de medidas

m = float (input('Digite a quantidade de metro: '))
cm = m * 100
mm = m * 1000
print('O valor do metro digitado foi: {}m em centímetros equivale à: {:.0f}cm e em milímetros à: {:.0f}mm'.format(m,cm,mm))

num1 = int (input('Digite um número: '))
num2 = int (input('Digite outro número: '))
s = num1 + num2
sb = num1 - num2
mt = num1 * num2 
dv = num1 / num2
p = num1 ** num2
rs = num1 % num2
di = num1 // num2
rq1 = num1 **(1/2)
rq2 = num2 **(1/2)
print('A soma dos dois valores resulta em: {}\n A subtração dos dois valores resulta em: {}\n A multiplicação dos dois valores resulta em: {}\n A divisão dos dois valores resulta em: {}\n A exponenciação dos valores resulta em {:.3f}\n O resto da divisão entre os valores resulta em: {}\n A divisão por inteiro entre os valores resulta em: {}\n A raiz quadrada do primeiro número é de: {:.3f}\n A raiz quadrada do segundo número é de: {:.3f}'.format(s,sb,mt,dv,p,rs,di,rq1,rq2))

# aula 04 de digitar com as chaves como formato
nome = str(input('Digite seu nome: '))
print('Seja Bem Vindo {}! Prazer em te conhecer'.format(nome))

