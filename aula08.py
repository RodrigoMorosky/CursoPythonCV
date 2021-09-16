# aula 8 utilizando módulos
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# dá para importar só a função desejada e não a biblioteca inteira
#from math import sqrt
#num = int(input('Digite um número: '))
#raiz = sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
