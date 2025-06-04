import pandas as pd

# Lê os dois arquivos
df1 = pd.read_excel('data.xlsx')
df2 = pd.read_excel('data2.xlsx')

# Remove espaços extras dos títulos
df1['title1'] = df1['title1'].str.strip()
df2['title2'] = df2['title2'].str.strip()

# Cria um dicionário de mapeamento: {title2: codigo2}
codigo_map = dict(zip(df2['title2'], df2['codigo2']))

# Aplica a substituição condicional: se o título de df1 está em df2, substitui o código
df1['codigo1'] = df1['title1'].apply(
    lambda titulo: codigo_map[titulo] if titulo in codigo_map else df1.loc[df1['title1'] == titulo, 'codigo1'].values[0]
)

# Salva o próprio df1 de volta como data_corrigido.xlsx
df1.to_excel('data_corrigido.xlsx', index=False)
