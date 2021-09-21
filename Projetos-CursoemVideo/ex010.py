# Programa que informa quantos dólares podem ser comprados, considerando US$1,00 = R$3,27

print('Esse software lhe informa quantos dólares podem ser comprados,\nconsiderando US$1,00 = R$3,27')
reais = float(input('Informe quantos reais você possui: R$'))
print('\nCom esse dinheiro você consegue comprar {:.2f} dólares.'.format(reais/3.27))
