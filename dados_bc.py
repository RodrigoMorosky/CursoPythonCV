import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (16,8)

def consulta_bc(codigo_bcb):
  url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
  df = pd.read_json(url)
  df['data'] = pd.to_datetime(df['data'], dayfirst=True)
  df.set_index('data', inplace=True)
  return df

ipca = consulta_bc(433)
igpm = consulta_bc(189)
selic_meta = consulta_bc(432)
cdi = consulta_bc(12)
reservas_internacionais = consulta_bc(13621)
pnadc = consulta_bc(24369)
concessoes_t = consulta_bc(20631)
concessoes_pf = consulta_bc(20633)
concessoes_pj = consulta_bc(20632)
divida_externa = consulta_bc(21535)
dlsp_govebcb = consulta_bc(2053)
divli_interna = consulta_bc(2063)
pib = consulta_bc(4382)
div_pib = divli_interna / pib

ipca.plot()
igpm.plot()
selic_meta.plot()
cdi.plot()
reservas_internacionais.plot()
divida_externa.plot()
dlsp_govebcb.plot()
divli_interna.plot()
pnadc.plot()
concessoes_t.plot()
concessoes_pj.plot()
concessoes_pf.plot()

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1).plot(ipca.loc['2000-01-01':'2020-10-28'])
ax2 = fig.add_subplot(2,2,2).plot(selic_meta.loc['2000-01-01':'2020-10-28'])
ax3 = fig.add_subplot(2,2,3).plot(reservas_internacionais.loc['2000-01-01':'2020-10-28'])
ax4 = fig.add_subplot(2,2,4).plot(divida_externa.loc['2000-01-01':'2020-10-28'])

divli_interna.loc['2010-01-01':'2020-07-01'].plot()
div_pib.loc['2010-01-01':'2020-07-01'].plot()
