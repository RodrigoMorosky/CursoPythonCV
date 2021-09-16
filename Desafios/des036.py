casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual é o seu salário mensal? '))
anos = int(input('Em quantos anos vai financiar o imóvel? '))
parcela = casa / (anos *12)
if parcela < 0.3 * salario:
    print('Você poderá financiar sua casa com parcela de \033[34m{}\033[m'.format(parcela))
else:
    print('\033[31mInfelizmente você não poderá financiar sua casa pois a parcela de \033[33m{} \033[31mé maior do que 30% do seu salário de {}\033[m'.format(parcela, salario))