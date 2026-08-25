import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title='SuperStore - Análise de Vendas', layout='wide')
st.title('📊 Análise de Vendas - SuperStore')
st.write('Dashboard com os principais achados da análise exploratória (EDA) do dataset SuperStore.')

sns.set_theme(style='darkgrid')

# --- CARREGANDO OS DADOS ---
df = pd.read_csv('SuperStoreOrders.csv')
df['sales'] = df['sales'].astype(str).str.replace(',', '', regex=False)
df['sales'] = pd.to_numeric(df['sales'])
df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True)
df['ship_date'] = pd.to_datetime(df['ship_date'], format='mixed', dayfirst=True)

st.divider()

# --- VISÃO GERAL DE VENDAS ---
st.header('Visão geral de vendas')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Por Segmento')
    sales_per_segment = (df.groupby('segment')['sales']
                        .sum()
                        .sort_values(ascending=False))
    
    fig, ax = plt.subplots(figsize=(5, 4))

    ax.bar(sales_per_segment.index, 
           sales_per_segment.values, 
           color='seagreen', 
           alpha=0.8)
    
    ax.set_ylabel('Vendas ($)')
    plt.xticks(rotation=20)
    st.pyplot(fig)

with col2:
    st.subheader('Por País - Top 5')
    sales_per_country = (df.groupby('country')['sales']
                        .sum()
                        .sort_values(ascending=False)
                        .head(5))
    
    fig, ax = plt.subplots(figsize=(5, 4))

    ax.bar(sales_per_country.index, 
           sales_per_country.values, 
           color='steelblue', 
           alpha=0.8)

    ax.set_ylabel('Vendas ($)')
    plt.xticks(rotation=20)
    st.pyplot(fig)

with col3:
    st.subheader('Por Estado - Top 5')
    sales_per_state = (df.groupby('state')['sales']
                       .sum()
                       .sort_values(ascending=False)
                       .head(5))
    
    fig, ax = plt.subplots(figsize=(5, 4))

    ax.bar(sales_per_state.index, 
           sales_per_state.values, 
           color='indianred', 
           alpha=0.8)

    ax.set_ylabel('Vendas ($)')
    plt.xticks(rotation=20)
    st.pyplot(fig)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Por Região - Top 5')
    sales_per_region = (df.groupby('region')['sales']
                        .sum()
                        .sort_values(ascending=False)
                        .head(5))
    
    fig, ax = plt.subplots(figsize=(5, 4))

    ax.bar(sales_per_region.index, 
           sales_per_region.values, 
           color='grey', 
           alpha=0.8)

    ax.set_ylabel('Vendas ($)')
    plt.xticks(rotation=20)
    st.pyplot(fig)

with col2:
    st.subheader('Por Categoria')
    sales_per_category = (df.groupby('category')['sales']
                          .sum()
                          .sort_values(ascending=False))
    
    fig, ax = plt.subplots(figsize=(5, 4))

    ax.bar(sales_per_category.index, 
           sales_per_category.values, 
           color='goldenrod', 
           alpha=0.8)

    ax.set_ylabel('Vendas ($)')
    plt.xticks(rotation=20)
    st.pyplot(fig)

with col3:
    st.subheader('Por Subcategoria - Top 5')
    sales_per_sub_category = (df.groupby('sub_category')['sales']
                              .sum()
                              .sort_values(ascending=False)
                              .head(5))
    
    fig, ax = plt.subplots(figsize=(5, 4))
    
    ax.bar(sales_per_sub_category.index, 
           sales_per_sub_category.values, 
           color='mediumpurple', 
           alpha=0.8)
    
    ax.set_ylabel('Vendas ($)')
    plt.xticks(rotation=20)
    st.pyplot(fig)

st.divider()

# --- VENDAS E LUCRO POR ANO ---
st.header('Desempenho por ano')

sales_per_year = df.groupby('year')['sales'].sum().sort_index()
profit_per_year = df.groupby('year')['profit'].sum().sort_index()

col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots(figsize=(7, 5))

    sns.lineplot(x=sales_per_year.index, 
                 y=sales_per_year.values,
                 ax=ax, 
                 color='red', 
                 marker='o', 
                 markersize=7, 
                 linewidth=2)
    
    ax.set_title('Vendas por ano', fontweight='bold')
    ax.set_xlabel('Período')
    ax.set_ylabel('Vendas ($)')
    st.pyplot(fig)

with col2:

    fig, ax = plt.subplots(figsize=(7, 5))

    sns.lineplot(x=profit_per_year.index, 
                 y=profit_per_year.values,
                 ax=ax, marker='o', 
                 markersize=7, 
                 linewidth=2)
    
    ax.set_title('Lucro por ano', fontweight='bold')
    ax.set_xlabel('Período')
    ax.set_ylabel('Lucro ($)')
    st.pyplot(fig)

st.divider()

# --- CORRELAÇÕES ---
st.header('Correlações')

col1, col2 = st.columns(2)

with col1:
    pearson = df[['sales', 'profit']].corr(method='pearson')

    fig, ax = plt.subplots(figsize=(5, 4))

    sns.heatmap(pearson, 
                annot=True, 
                cbar=False, 
                cmap='coolwarm', 
                vmin=-1, 
                vmax=1, 
                ax=ax)
    
    ax.set_title('Vendas x Lucro (Pearson)', fontweight='bold')
    st.pyplot(fig)

with col2:
    spearman = df[['discount', 'profit']].corr(method='spearman')
    
    fig, ax = plt.subplots(figsize=(5, 4))

    sns.heatmap(spearman, 
                annot=True, 
                cbar=False, 
                cmap='mako', 
                vmin=-1, 
                vmax=1, 
                ax=ax)
    
    ax.set_title('Desconto x Lucro (Spearman)', fontweight='bold')
    st.pyplot(fig)

st.divider()

# --- LUCRO POR SUBCATEGORIA ---
st.header('Lucro por Subcategoria')

profit_per_subcategory = (df.groupby('sub_category')['profit']
                          .sum()
                          .sort_values(ascending=False))

fig, ax = plt.subplots(figsize=(12, 5))

sns.barplot(x=profit_per_subcategory.index, 
            y=profit_per_subcategory.values,
            hue=profit_per_subcategory.index, 
            legend=False, 
            ax=ax)

ax.axhline(y=0, 
           color='black', 
           linestyle='--', 
           linewidth=1)

ax.set_xlabel('Subcategoria')
ax.set_ylabel('Lucro ($)')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

st.divider()

# --- IMPACTO DO DESCONTO NO LUCRO ---
st.header('Impacto do desconto no lucro')


def classificar_desconto(desconto):
    if desconto == 0:
        return '0%'
    elif desconto <= 0.1:
        return '0-10%'
    elif desconto <= 0.2:
        return '10-20%'
    elif desconto <= 0.3:
        return '20-30%'
    elif desconto <= 0.5:
        return '30-50%'
    else:
        return '50%+'


df['faixa_desconto'] = df['discount'].apply(classificar_desconto)

profit_per_discount = (df.groupby('faixa_desconto')['profit']
                       .mean()
                       .reindex(['0%', '0-10%', '10-20%', '20-30%', '30-50%', '50%+']))

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(profit_per_discount.index, 
       profit_per_discount.values, 
       color='orange', 
       alpha=0.85)

ax.axhline(y=0, 
           color='black', 
           linestyle='--', 
           linewidth=1)

ax.set_xlabel('Faixa de desconto')
ax.set_ylabel('Lucro médio ($)')
st.pyplot(fig)

st.caption(
    'A partir de 20% de desconto, o lucro médio por pedido vira negativo, '
    'chegando a -$99 em média nos pedidos com desconto acima de 50%.'
) 