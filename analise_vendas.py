#%%
# IMPORTAÇÀO DE LIBS

import pandas as pd
import numpy as np

# %%
# CARREGANDO OS DADOS

df = pd.read_csv('SuperStoreOrders.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)

# %%
#  --- CONHECENDO A BASE - LEVANTAMENTO DE DADOS ---

# PRIMEIROS REGISTROS 
df.head()

# %%

# VERIFICANDO COLUNAS
print(df.columns) 

# %%

# VERIFICANDO DTYPES
df.info()

# %%

# DIMENSÕES DA BASE
df.shape

# %%

# VERIFICANDO VALORES NULOS
df.isna().sum()

# %%

# VERFICANDO SE HÁ REGISTROS DUPLICADAS
df.duplicated().sum()

# %%

# VERFICANDO ESTATÍSTICAS GERAIS
df.describe()

# %%

# QUANTIDADE DE VALORES ÚNICOS
df.nunique()

# %%

# FREQUÊNCIA DAS CATEGORIAS 
df['category'].value_counts()

# %%

# FREQUÊNCIA DOS PAÍSES
df['country'].value_counts()

# %%

# FREQUÊNCIA DOS SEGMENTOS
df['segment'].value_counts()

# %%
# --- LIMPEZA E TRATAMENTO DE DADOS ---

# CORRIGINDO DTYPES DE DATAS
df['order_date'] = pd.to_datetime(df['order_date'], format = 'mixed', dayfirst= True)

df['ship_date'] = pd.to_datetime(df['ship_date'], format = 'mixed', dayfirst= True)

df[['order_date', 'ship_date']]

# %%

# CORRIGINDO DTYPES DE VENDAS

df['sales'] = df['sales'].astype(str).str.replace(',', '', regex= False)

df['sales'] = pd.to_numeric(df['sales'])

df['sales'].head(10)

# %%

# VERIFICANDO AS DATAS ESTÃO COERENTES
df.query('ship_date < order_date')[['order_date', 'ship_date']]

# %%

# VERIFICANDO VENDAS ZERADAS OU NEGATIVAS

sales_is_0 = df.query('sales <= 0')
sales_is_0.shape[0]

# %%

# VERIFICANDO QUANTIDADES ZERADAS OU NEGATIVAS

quantity_is_0 = df.query('quantity <= 0')
quantity_is_0.shape[0]

# %%

# VERIFICANDO CUSTO DE ENVIO ZERADOS OU NEGATIVOS

shipping_cost_0 = df.query('shipping_cost <= 0')
shipping_cost_0.shape[0]

# %%

# VERIFICANDO LUCRO NEGATIVO

profit_under_0 = df.query('profit < 0')
profit_under_0.shape[0]

