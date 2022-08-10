# Bibliotecas Utilizadas:
import pandas as pd

# Importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Visualizar base de dados
pd.set_option('display.max_columns', None)
# print(tabela_vendas)

# Faturamento por Loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# Quantidade de produtos vendidos por loja


# Ticket médio por produto em cada loja


# Enviar um email por produto em cada loja
