# Método para converter linhas de um csv em json
def csvToJson(dataframe):
    chaves = dataframe.keys()
    lista = []

    for index, row in dataframe.iterrows():
        dicionario = {}
        for key in chaves:
            dicionario[key] = row[key]

        lista.append(dicionario)

    return lista