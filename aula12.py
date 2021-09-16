# Condições aninhadas:
# condição IF com mais de duas...
# if carro.esquerda():
# elif carro.direita():
# elif carro.re(): #pode ter vários ELIF
# else: o ELSE é opcional!

nome = str(input('Qual é o seu nome? '))

if nome.lower() == 'rodrigo' or nome.lower() =='daniel':
    print('\033[34mQue nome lindo você tem!\033[m')
elif nome.lower() == 'erika' or nome.lower() == 'maria':
    print('\033[35mVixe lá vem!!!\033[m')
else:
    print('\033[32mSeu nome é bem normal.\033[m')
print('Tenha um bom dia, \033[31m{}\033[m!'.format(nome.title()))