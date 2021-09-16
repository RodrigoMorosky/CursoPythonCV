n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor'))

s1 = n1+n2
s2 = n1-n2
s3 = n1*n2
s4 = n1/n2
s5 = n1**n2
s6 = n1//n2
s7 = n1%n2

print('A soma de {0} e {1} é {2}'.format(n1, n2, s1))
print('A subtração de {0} e {1} é {2}'.format(n1, n2, s2))
print('A multiplicação de {0} e {1} é {2}'.format(n1, n2, s3))
print('A divisão de {0} e {1} é {2:.3f}'.format(n1, n2, s4))
print('A potência de {0} e {1} é {2}'.format(n1, n2, s5))
print('A divisão inteira de {0} e {1} é {2}'.format(n1, n2, s6))
print('O resto da divisão de {0} e {1} é {2}'.format(n1, n2, s7))

# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // divisão inteira
# % resto da divisão

# Ordem de precedência para cálculo
# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - +, -

