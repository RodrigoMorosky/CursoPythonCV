n = int(input('Digite um número inteiro para saber sua tabuada: '))
m = 1
for c in range (1,11):
    print('\033[33m{}\033[m x \033[33m{}\033[m = \033[1;34m{}\033[m'.format(n, m, n*m))
    m = m+1