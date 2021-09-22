# Programa que informa a quantidade de tinta necessária para pintar uma parede

print('=======Tinta necessária para pintar uma parede=======\n')

print('Em metros,')
largura = float(input('Informe a largura da parede: '))
comprimento = float(input('Informe o comprimento da parede: '))
area = largura*comprimento

print('\nConsiderando que 1l de tinta pinta 2m²;')
print('E sua parede possui uma dimensão de {}x{}, ou seja, {}m²;'.format(largura, comprimento, area))
print('Você precisará de {}l de tinta.'.format(area/2))
