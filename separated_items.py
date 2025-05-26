import pandas as pd

# Carregar as planilhas
base_dados = pd.read_excel('estoqueX.xlsx')
dados_moto = pd.read_excel('lista_motos.xlsx')

# Obter o número de linhas e colunas das planilhas
n_row_base_dados, n_column_base_dados = base_dados.shape
n_row_dados_moto, n_column_dados_moto = dados_moto.shape

# Lista para armazenar os valores de códigos das motos do dados_moto
lista_indice_dados_moto = []

# Preencher a lista com os valores da coluna que você quer comparar
for linha in range(n_row_dados_moto):
    value = dados_moto.iloc[linha, 1]  # Supondo que o código está na segunda coluna (índice 1)
    lista_indice_dados_moto.append(value)

# Lista para armazenar as linhas da base de dados que correspondem aos códigos
linhas_correspondentes = []

# Iterar sobre cada linha da base de dados
for i, row in base_dados.iterrows():
    dados_da_linha = row.to_dict()  
    
    # Verificar se o código (assumindo que o código está na primeira coluna) está na lista de dados_moto
    if dados_da_linha['Código'] in lista_indice_dados_moto:  # Substitua 'codigo' pela coluna correta, se necessário
        linhas_correspondentes.append(dados_da_linha)

# Converter a lista de linhas correspondentes para um DataFrame
df_correspondentes = pd.DataFrame(linhas_correspondentes)

# Salvar as linhas correspondentes em um novo arquivo Excel
df_correspondentes.to_excel('motos_correspondentes.xlsx', index=False)

