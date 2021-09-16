# estrutura de repetição while (enquanto)
#for c in range(1, 10):
#    print(c)
#print('FIM')

c = 1
while  c <= 10:
    print(c)
    c = c + 1
print('FIM')

n = 1
while n != 0: # diferente
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')

e = 1
par = inpar = 0
while e != 0:
    e = int(input('Digite um valor:'))
    if e != 0:
        if e % 2 == 0:
            par += 1
        else:
            inpar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, inpar))