import tabula as tb
import csv
import pandas as pd

saida = r"C:\Users\rodri\Dropbox\temporário Morosky Advocacia\SUP. BOBBIO\AI 5.072.144-4\saida.csv"
arquivo = r"C:\Users\rodri\Dropbox\temporário Morosky Advocacia\SUP. BOBBIO\AI 5.072.144-4\5 - Demonstrativo do Auto de Infração (Analítico).pdf"
pasta = "Área de Trabalho"
pdf = tb.read_pdf(arquivo, pages='1')

with open(r"C:\Users\rodri\Dropbox\temporário Morosky Advocacia\SUP. BOBBIO\AI 5.072.144-4\saida.csv", 'w', newline='') as saida:
#    escrever = csv.writer(saida)
#    for i in pdf:
#        escrever.writerows([i])

    tb.convert_into(pdf, 'teste.csv', output_format='csv')
#df = pd.DataFrame(tb.read_pdf(arquivo, pages='1'))
#df.to_excel('output.xlsx')
#print(df)