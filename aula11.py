# aula 11 - cores no terminal
# \033[ style, text, back m
# style - 0 (nome), 1 (bold), 4 (underline), 7 (negative)
# text - 30 - branco, 31 - vermelho, 32 - verde, 33 - amarelo, 34 - azul, 35 - roxo, 36 - azul claro e 37 - cinza
# back - 40, 41, 42, 43, 44, 45, 46, 47 (mesma ordem do text)

print('\033[0;33;44mOlá mnudo\033[m')
a = 3
b = 5
print('Os valores são \033[32m{} e \033[31m{}\033[m!!'.format(a, b))
nome = 'Rodrigo'
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pb': '\033[7;30m'}
print('Este é mais um teste de cores {}{}{}!!!'.format(cores['pb'], nome, cores['limpa']))