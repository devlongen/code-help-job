import pandas as pd
#dataframes
df = pd.read_excel('estoqueJRM.xlsx')
comparar = pd.read_csv('marcas-motos.csv',delimiter=";")
modelo_dataset = pd.read_csv('models.csv',delimiter=",")


#linhas
n_row,n_column = df.shape
n_row_comparar,n_column_comparar = comparar.shape
n_row_modelo,n_column_modelo = modelo_dataset.shape


# dist
dicionario_produto = {}

#listas
lista_produto = []
lista_marca_comparativo = []
lista_correta = []
lista_modelo_comparativo=[]
lista_sem_modelo = []

#loops
for i in range(n_row):
    marcas = df.iloc[i,7]
    titulo = df.iloc[i,2]
    codigo = df.iloc[i,0]
    modelo = df.iloc[i,8]
    dicionario_produto = {"codigo":codigo,"titulo":titulo,"marcas":marcas,"modelo":modelo}
    lista_produto.append(dicionario_produto)

for j in range(n_row_comparar):
    value = comparar.iloc[j,1]
    lista_marca_comparativo.append(value)

for z in range(n_row_modelo):
    value = modelo_dataset.iloc[z,0]
    lista_modelo_comparativo.append(value)
    
# Itens que estão de acordo com a marca

for produto in lista_produto:
    if produto["marcas"] in lista_marca_comparativo:
        lista_sem_modelo.append(produto)
        df_output1 = pd.DataFrame(lista_sem_modelo)
        df_output1.to_excel('lista_de_motos_sem_modelos.xlsx')
    else:
        print(None)

# Itens que são parecido 