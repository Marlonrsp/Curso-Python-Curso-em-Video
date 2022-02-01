# Seno, Cosseno e Tangente
from math import radians, sin, cos, tan

an = float(input('Digite o angulo ao qual você deseja: '))
sen = sin(radians(an))
print('O ângulo de {} tem o Seno de {:.2f} '.format(an,sen))
co = cos(radians(an))
print('O ângulo de {} é consseno de {:.2f}'.format(an,co))
ta = tan(radians(an))
print('O ângulo de {} é tangente de {:.2f}'.format(an,ta))