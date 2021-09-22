# Programa que converte metros em medidas       

print('Conversor de metros\n')
medida = float(input('Insira uma medida em metros: '))
print('Essa medida correponde a\nQuilômetros: {:.2f}\nHectômetros: {:.2f}\nDecâmetros: {:.2f}\nDecímetros: {:.2f}\nCentímetros: {:.2f}\nMilímetros: {:.2f}'.format(medida/1000, medida/100, medida/10, medida*10, medida*100, medida*1000))
