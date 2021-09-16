import math
co = int(input('Qual o comprimento do cateto oposto? '))
ca = int(input('Qual o comprimento do cateto adjacente? '))
hi = math.sqrt(co**2 + ca**2)
print('A hipotenusa desse triângulo é {} \n cateto oposto {} \n cateto adjacente {}'.format(hi, co, ca))