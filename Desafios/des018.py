import math
n = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('Do ângulo {} temos: \n seno > {:.2f} \n coseno > {:.2f} \n tangente > {:.2f}'.format(n, sen, cos, tan))