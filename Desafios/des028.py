import random
n = random.randint(0,5)
print('Estou pensando em um número...')
a = int(input('Tente adivinhar qual número estou pensando entre 0 e 5: '))
if a == n:
    print('Parabéns você adivinhou que eu pensei o número {}'.format(n))
else:
    print('Errou! Estava pensando no número {}'.format(n))