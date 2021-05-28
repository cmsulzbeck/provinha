import pandas as pd
import os

from pandas.core import base

# Importando bases
caminho = os.getcwd() + "\\bases"

airBnbNy2019 = pd.read_csv(f"{caminho}/airbnb_ny_2019.csv")

mapeamentoVizinhanca = pd.read_csv(f"{caminho}/mapeamento_vizinhanca.csv", ';')

# Removendo duplicatas
airBnbNy2019.drop_duplicates(keep=False,inplace=True)

mapeamentoVizinhanca.drop_duplicates(keep=False,inplace=True)

# Removendo linhas nulas
airBnbNy2019.dropna(inplace=True)

mapeamentoVizinhanca.dropna(inplace=True)

# Juntando bases
base_merge = pd.merge(airBnbNy2019, mapeamentoVizinhanca, left_on='neighbourhood', right_on='vizinhanca')

# Removendo coluna 'vizinhanca'
base_merge.drop('vizinhanca', axis='columns', inplace=True)

# Renomeando colunas
base_merge.rename(columns={'vizinhanca_grupo': 'neighbourhood_group'}, inplace=True)

# Filtrando valores de neighbourhood_group
filtro = ['Brooklyn', 'Manhattan', 'Queens', 'Staten Island']

base_merge = base_merge[base_merge.neighbourhood_group.isin(filtro)]

# Enviando para csv
base_merge.to_csv(f"{caminho}\\residencias.csv")

# Gerando base media_preco.csv
# Associando com base teste
base_dummy = base_merge[["neighbourhood_group", "room_type", "price"]]

# Agrupando por grupo de vizinhança e tipo de quarto e tirando a média
media_preco = base_dummy.groupby(["neighbourhood_group", "room_type"]).mean()
print(media_preco)

# Exportando para csv
media_preco.to_csv(f"{caminho}\\media_preco.csv")