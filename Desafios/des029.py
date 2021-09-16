velocidade = int(input('Qual a velocidade do carro: '))
v = velocidade - 80
m = v* 7
if v >=1:
    print('Você foi multado em R${}'.format(m))
else:
    print('OK!')