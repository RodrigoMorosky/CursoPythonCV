# laços, repetições e iterações
#Laços de repetição
# for a in range(x,y,z): o python não considera o último número!
# x = início da contagem
# y = fim da contagem
# z = pula na contagem

#for c in range(0,6):
 #   print(c)
#print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1, p):
    print(c)
print('Fim!')