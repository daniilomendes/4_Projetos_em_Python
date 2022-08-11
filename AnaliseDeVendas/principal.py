# Bibliotecas Utilizadas:
import pandas as pd
from enviar_email import enviar_email

# Importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Visualizar base de dados
pd.set_option('display.max_columns', None)
# print(tabela_vendas)

print('----------------------Faturamento por Loja-----------------------\n')
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
# print(faturamento)

print('-------------Quantidade de produtos vendidos por loja------------\n')
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
# print(quantidade)

print('--------------Ticket Médio por produto em cada loja--------------\n')
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
# print(ticket_medio)

# Enviar um email com o relatório
enviar_email(faturamento, quantidade, ticket_medio)
