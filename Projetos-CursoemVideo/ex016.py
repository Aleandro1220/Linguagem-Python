# Programa que apresenta a parte inteira de um número

from math import floor
print('-----Parte inteira de um número-----')
num = float(input('Informe um valor qualquer: '))
print('Sua parte inteira é {}'.format(floor(num))) # Ou usando o math.trun(num) # Ou int(num)
