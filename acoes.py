from datetime import date
from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

# Indice Ibovespa
#cotacao_bovesba = web.DataReader('^BVSP', data_source='yahoo', start='01/09/2022', end='30/09/2022')
#print(cotacao_bovesba)

tabela_empresas = pd.read_excel("Empresas.xlsx")
#print(tabela_empresas)

for empresa in tabela_empresas['Empresas']:
    print(f'Cotação da ação {empresa}')
    cotacao = web.DataReader(f'{empresa}.SA', data_source='yahoo', start=date(2022,9,1), end=date(2022,9,21))
    print(cotacao)
    # df = pd.DataFrame(cotacao['Adj Close'])
    # print(df)
    #print(cotacao.tail)
    #print(cotacao['Adj Close'])
    # if cotacao['Adj Close'] >= 11:
    #     print('comprar')
    cotacao['Adj Close'].plot()
    plt.show()

# lista_empresa = ['ITUB4','PETR4', 'VALE3']

# for empresa in lista_empresa:
#     print(f'Cotação da ação {empresa}')
#     cotacao = web.DataReader(f'{empresa}.SA', data_source='yahoo', start='01/09/2022', end='30/09/2022')
#     print(cotacao)
#     cotacao['Adj Close'].plot()
#     plt.show()

