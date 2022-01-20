salario = float(input('Qual o salário do funcionário: R$'))
aumento = salario + (salario * 15 / 100)
print('O salario do funcionario era de R$ {:.2f} ,e com o aumento de 15% passa a ser de R$ {:.2f} '.format(salario, aumento))
