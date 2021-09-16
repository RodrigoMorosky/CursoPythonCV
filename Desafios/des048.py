s = 0
for c in range(1,500):
    if c %2 >0:
        if c %3 == 0:
            s = s+c
print('A soma de todos os números ímpares entre 1 e 500 é \033[35m{}\033[m'.format(s))