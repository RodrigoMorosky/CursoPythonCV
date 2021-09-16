n = 0
c = 1
while True:
    n = int(input('Digite um número para saber sua tabuada (número negativo para sair): '))
    if n <=0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
        c +=1
print('Programa encerrado!')