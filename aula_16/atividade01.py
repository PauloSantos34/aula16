# tb_vendas.csv
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os
load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')

# Conexão com o banco de dados
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


# Buscando dados
# Leitura da tabela de vendas
df_vendas = pd.read_sql('tb_vendas', engine)
print(df_vendas.head())  # Mostra os dados

# Calcular o valor da venda - Criar a série "coluna" valor_venda
df_vendas['valor_venda'] = df_vendas['qtd'] * df_vendas['preco']

# Cria nova coluna com comissão (10%)
df_vendas['comissao'] = (df_vendas['valor_venda'] * 0.09).round(2)
# Mostra o DataFrame com a nova coluna
print(df_vendas[['nome_vendedor', 'valor_venda', 'comissao']])

# ARRAY NUMPY
# Converte para array
array_valor_vendas = np.array(df_vendas['valor_venda'])

# Calcula média e mediana
media = np.mean(array_valor_vendas)
mediana = np.median(array_valor_vendas)
distancia = abs(media - mediana) / mediana 

# MEDIDAS DE TENDÊNCIA CENTRAL
print('\nMEDIDAS DE TENDÊNCIA CENTRAL')
print(f"Média das comissões: R$ {media:.2f}")
print(f"Mediana das comissões: R$ {mediana:.2f}")
print({distancia})
