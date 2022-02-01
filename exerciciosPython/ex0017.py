# catetos e hipotenusa

# Somente com cálculo matemático 

# co = float (input('Comprimento do cateto oposto: '))
# ca = float (input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hi))


# Com importação

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjecente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
