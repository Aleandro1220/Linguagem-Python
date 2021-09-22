# Programa que calcula o total a ser pago num alugel de carros

print('----------Alguel de carros----------')
print('\nInsira as informações sobre o carro alugado.')
dia = int(input('Dias de uso: '))
km = float(input('Quilômetros rodados: '))
conta = (km*0.15) + (60*dia)

print('O valor a ser pago por {}km e {} dia(s)\né de R${:.2f}'.format(km, dia, conta))
