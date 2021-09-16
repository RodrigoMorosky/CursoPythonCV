# aula sobre manipulação de texto
# função len retorna o número de caractéres que a string tem
# count('o') vai contar quantas vezes aparece determinado caractere
# find() vai retornar a posição em que começou o que se está procurando, se não encontra retorna -1
# o operador 'in' vai retornar verdadeiro ou falso na string
## replace('Python', 'Android') vai subistituir a palavra python por android na string
# upper() - vai colocar em maiúsculo
# lower() - vai colocar me minúsculo
# capitalize() - vai colocar só o primeiro caractere em maiúsculo e o resto em minúsculo
# title() - vai analisar quantas palavras tem na string e vai colocar o primeiro caractere em maiúsculo
# strip() - vai remover os esp/aços inúteis no início e no final da string
# rstrip() - vai remover os espaços inúteis do lado direito da string
# lstrip() - vai remover os espaços inúteis do lado esquerdo da string
# split() - vai fazer uma divisão onde houver espaços na string e gerar uma lista com as strings
# '-'.join(frase) - vai juntar as strings com o caractere entre aspas simples

frase = 'Curso em Vídeo Python'
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('video'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

#print("""A reunião com Millenium está agendada para segunda.
#Estou aguardando a data da reunião da Composé que eles ainda não confirmaram. Mas será na próxima semana.
#Estamos finalizando o relatório da Belmax para agendar a reunião com eles também.""")