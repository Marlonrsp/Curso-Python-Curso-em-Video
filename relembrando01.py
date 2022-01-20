# media de notas
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
print('A média do aluno é de: {}'.format(media))

# dobro, triplo, raiz quadrada, raiz cúbica

n = float(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
rc = n ** (1/3)
print('O número digitado foi: {0}\n O dobro dele é de: {1}\n O triplo dele é de: {2}\n A raiz quadrada é: {3}\n A raiz cúbica é de: {4}'.format(n,d,t,r,rc))

# sucessor e antecessor do número

n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print('O número digitado foi: {0}\n Seu sucessor é: {1}\n Seu antecessor é: {2}'.format(n,s,a))

# tipos de reconhecimento de variáveis

# tipo string 
n = str(input('Digite algo: '))
print (type(n))

#tipo int
a = int(input('Digite algo: '))
print (type(a))

#tipo float
f = float(input('Digite algo: '))
print(type(f))

