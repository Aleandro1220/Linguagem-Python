# Programa que apresenta o seno, cosseno e tangente de um ângulo

from math import radians, sin, cos, tan

print('------Seno, cosseno e tangente------\n')
num = float(input('Insira o valor de um ângulo: '))
num = radians(num)
print('\nEis as especificações:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin(num), cos(num), tan(num)))
