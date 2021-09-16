# variaveis compostas (Tuplas)
# três tipos de variáveis compostas - Tuplas, listas, Dicionários
# os elementos são identificados por índices apartir do 0
# as Tuplas são imutáveis
# () - tuplas ; [] - lista ; {} - dicionário

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-1])
print(lanche[-3:])

for i in lanche:
    print(i)