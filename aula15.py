# interrompendo repetições while (break)

cont = 1
while cont <= 10:
    print(cont, '->', end='')
    cont +=1
print('--FIM--')

#cont = 1
#while True:
#    print(cont, '->', end='')
#    cont +=1
#print('--FIM--')

n = s = 0
while n != 999:
    n = int(input('Digite um núemro: '))
    s += n
s -= 999 # gambiarra para não somar o 999
print('A soma vale {}'.format(s))

n = s = 0
while True:
    n = int(input('Digite um núemro: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # nova forma F string
