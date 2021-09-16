a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = 0

while c != 5:
    print('O que você quer fazer com esses números? \n'
          '[1] Somar \n'
          '[2] Multiplicar \n'
          '[3] Maior \n'
          '[4] Novos números \n'
          '[5] Sair do programa')
    c = int(input())
    if c == 1:
        print(a + b)
    elif c == 2:
        print(a * b)
    elif c == 3:
        if a - b >0:
            print(a)
        else:
            print(b)
    elif c == 4:
        a = int(input('Digite um número: '))
        b = int(input('Digite outro número: '))
    elif c == 5:
        print('Saindo...')