import pandas as pd
path = '/content/drive/MyDrive/covid_data.csv'

# supondo que eu sei o intervalo da linha buscado
chunk_size = 100000 # limite da busca (retornado da arvore)
linha_buscada = 238711
linha_inicial_busca = chunk_size * (int(linha_buscada/chunk_size)) # retorna o indice inicial da linha buscada
retorno = ''
conta_linhas = 0
for linha in pd.read_csv(path, chunksize = chunk_size, skiprows= linha_inicial_busca - 1):
    conta_linhas += 1
    if conta_linhas == linha_buscada:
        retorno = linha
        break

