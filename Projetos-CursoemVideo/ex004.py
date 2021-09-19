# Brincando com o comando "is", informando o tipo primitivo de uma inserção qualquer

print('\nEsse program informa o tipo primitivo do que for inserido.')
var = input('Digite alguma coisa: ')

print('O valor digitado é', type(var))
print('\nSegue a lista de especificidades do termo:\n')
print('Decimal:', var.isdecimal())
print('Afabético:', var.isalpha())
print('Numérico:', var.isnumeric())
print('Alfanumérico:', var.isalnum())
print('Ascii:', var.isascii())
print('Dígito:', var.isdigit())
print('Identificador:', var.isidentifier())
print('Minúsculo:', var.islower())
print('Maiúsculo:', var.isupper())
print('Imprimível:', var.isprintable())
print('Espaço:', var.isspace())
print('Capitalizada:', var.istitle())
