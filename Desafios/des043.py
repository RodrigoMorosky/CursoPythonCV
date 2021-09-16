altura = float(input('Qual é a sua alura em metros? (separe por \033[31m.\033[m e não por \033[31m,\033[m)'))
peso = float(input('Qual é o seu peso? separe por \033[31m.\033[m e não por \033[31m,\033[m )'))
imc = peso / (altura * altura)
if imc < 18.5:
    print('\033[30mVocê está abaixo do peso!\033[m ')
elif 18.5 < imc < 25:
    print('\033[32mVocê está no peso ideal!\033[m')
elif 25 < imc < 30:
    print('\033[33mVocê está com sobrepeso! \033[m')
elif 30 < imc < 40:
    print('\033[31mVocê está obeso! \033[m')
else:
    print('\033[35mVocê está com obesidade mórbida! \033[m')