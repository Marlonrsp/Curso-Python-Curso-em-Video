# pintar área da parede
l = float(input('Digite a largura da sua parede: '))
a = float(input('Digite a altura da sua parece: '))
ar = l * a
print('Sua parede tem a dimensão de {}x{} e a àrea de {:.3f}m².'.format(l,a,ar))
t = ar / 2
print('A quantidade necessária para pintar a parede é de {}l de tinta'.format(t))