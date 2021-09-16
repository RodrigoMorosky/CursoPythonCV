import PyPDF2 as pdf2
arquivo = r"C:\Users\rodri\Dropbox\temporário Morosky Advocacia\SUP. BOBBIO\AI 5.072.144-4\5 - Demonstrativo do Auto de Infração (Analítico).pdf"
pdf = open(arquivo, "rb")
lerPDF = pdf2.PdfFileReader(pdf)
npg = lerPDF.numPages
for i in range(0, npg):
    conteudo = lerPDF.getPage(i)
    print(conteudo.extract)

#pg = lerPDF.getPage(0)
#conteudo = pg.extractText()
#print(conteudo)