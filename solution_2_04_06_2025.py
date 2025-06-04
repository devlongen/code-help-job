import pandas as pd

# Lê os dois arquivos
df1 = pd.read_excel('data3.xlsx')
df2 = pd.read_excel('data2.xlsx')

# Remove espaços extras dos títulos
df1['titulo'] = df1['titulo'].str.strip()
df2['title2'] = df2['title2'].str.strip()

# Cria um dicionário de mapeamento: {title2: codigo2}
codigo_map = dict(zip(df2['title2'], df2['codigo2']))

# Preenche valores faltantes em 'codigo1' com base no título correspondente
df1['Codigo'] = df1.apply(
    lambda row: codigo_map[row['titulo']] if (pd.isna(row['Codigo']) or row['Codigo'] == '') and row['titulo'] in codigo_map else row['Codigo'],
    axis=1
)

# Salva o resultado
df1.to_excel('data_corrigido_2.xlsx', index=False)
