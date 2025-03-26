#%%
#Carregando Arquivo

with open('data.csv', encoding='utf-8') as open_file:
    data = open_file.readlines()

#Dicionário
dados = dict()

#Chaves
chaves = data[0].strip('\n').split(';')

for indice in chaves:
    dados[indice] = []

for linha in data[1:]:
    valores = linha.strip('\n').split(';')
    for i in range(len(chaves)):
        dados[chaves[i]].append(valores[i])

dados
