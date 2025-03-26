#%%
arquivo = 'data.csv'
#%%
with open(arquivo, encoding='utf-8') as open_file:
    data = open_file.readlines()

dados = dict()
chaves = data[0].strip('\n')
chaves

for i in chaves:
    dados[i] = []
dados

# %%
for linha in data[1:]:
    valores = linha.strip('\n').split(';')

# %%
