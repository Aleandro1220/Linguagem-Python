# Programa que informa o aumento salarial de um funcionário

print('-----Aumento salarial dos funcionários-----')
salario = float(input('Informe o salário atual de seu funcionário:\nR$'))
print('Após o reajuste de 15%, o salário de seu funcionário será de R${:.2f}'.format(salario*1.15))
