# Programa que informa a ordem de apresentação dos alunos

from random import shuffle

print('-----Ordem das apresentações-----\n')

al1 = input('Insira o nome do 1.º aluno: ')
al2 = input('Insira o nome do 2.º aluno: ')
al3 = input('Insira o nome do 3.º aluno: ')
al4 = input('Insira o nome do 4.º aluno: ')
als = [al1, al2, al3, al4]
shuffle(als)
print('\nA ordem de apresntação é a seguinte: {}.'.format(als))
