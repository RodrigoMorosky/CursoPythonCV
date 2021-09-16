# condições
tempo = int(input('Quantos anos tem seu carro: '))
if tempo <=3:
    print("Carro novo")
else:
    print("Carro velho")

print('Carro novo' if tempo<=3 else 'Carro velho')
print('--FIM--')

nome = str(input('Qual é o seu nome? '))
if nome.lower() == 'rodrigo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome não é Rodrigo')
print('Bom dia, {}'.format(nome))