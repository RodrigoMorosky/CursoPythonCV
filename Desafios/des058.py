import random
n = random.randint(0, 10)
print('Estou pensando em um número... tente adivinhar!')
a = 0
b = 0
while a != n:
    a = int(input('Digite o número: '))
    b = b + 1
print("Você tentou {} até acertar!".format(b))
