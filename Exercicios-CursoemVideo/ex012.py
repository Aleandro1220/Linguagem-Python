# Programa que informa o valor de um produto com 5% de desconto

print('Uma super liquidação irá ocorrer!\n')
valor = float(input('Informe o valor do produto: R$'))
print('Com 5% de desconto o produto custará R${:.2f}'.format(valor*0.95))
