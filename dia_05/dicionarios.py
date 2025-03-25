#%%
print('Dicionários')
lista = [1, 2, 3, 4, 5]
print(lista[0])

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': [1, 2, 3],
              'cargos': [{'nome': 'João', 'cargo': 'Analista'},
                         {'nome': 'Maria', 'cargo': 'Gerente'}]}
print(dicionario['cargos'][-1]['nome'])

dicionario['estado_civil'] = 'solteiro'

dicionario['cargos'].append({'nome': 'José', 'cargo': 'Diretor'})   
dicionario

dicionario.keys()
dicionario.values()
# %%

#%%
dicionario.items()


#%%

for i in dicionario:
    print(i, dicionario[i])

    #%%
for chave, valor in dicionario.items():
    print(chave, valor)    