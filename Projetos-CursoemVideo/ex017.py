# Calculando a hiptenusa com os módulos

from math import hypot

print('-----Descobrindo a hipotenusa de um triângulo-----\n')
cat1 = float(input('Informe o valor do 1.º cateto: '))
cat2 = float(input('Informe o valor do 2.º cateto: '))
print('A hipotenusa desse triângulo equivale a {:.2f}'.format(hypot(cat1, cat2)))
