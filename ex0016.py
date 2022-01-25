# quebrando um número

from math import trunc

num = float(input('Digite um valor: '))
print('O número digitado foi {} sendo que seu valor inteiro é {} '.format(num,trunc(num)))

# outra forma

n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a porção interira dele é de {} '.format(n, int(n)))


# testando com float 

n = int(input('Digite um número inteiro: '))
print('O número inteiro digitado foi {} e sua parte flutuante é de {:.2f} '.format(n, float(n)))
