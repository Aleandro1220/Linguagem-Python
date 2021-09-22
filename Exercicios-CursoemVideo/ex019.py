# Programa que auxilia um professor a sortear um dos alunos

from random import choice

print('Olá professor!\nEstá com difuculdade em sortear um aluno?\n')
al1 = input('Insira o nome do 1.º aluno: ')
al2 = input('Insira o nome do 2.º aluno: ')
al3 = input('Insira o nome do 3.º aluno: ')
al4 = input('Insira o nome do 4.º aluno: ')
als = [al1, al2, al3, al4]
print('\nO aluno escolhido para apagar a lousa foi: {}.'.format(choice(als)))