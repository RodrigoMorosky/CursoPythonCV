import pandas as pd

pasta = r'C:\Users\rodri\Dropbox\Sped\desenvolvimento\sped fiscal\27724509000133-080892051-20190201-20190228-0-D5036DF900A2196E450D5289892C9A26820C480C-SPED-EFD.txt'
arq = open(pasta, 'r+')
linha = [x.list() for x in arq]

linha