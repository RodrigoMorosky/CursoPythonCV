n = s = c = 0
while True:
    n = int(input('Deigite um valor (999 sair)'))
    if n ==999:
        break
    s += n
    c +=1
print(f'A soma dos {c} números é {s}!')