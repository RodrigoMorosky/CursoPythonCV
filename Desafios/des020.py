import random
# from random import shuffle - daí tem que tirar o random.
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
deck = [a1, a2, a3, a4]
random.shuffle(deck)
print('A ordem de apresentação será:')
print(deck)
