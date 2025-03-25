#%%
idades = [28,42,33,45,50,60,70,80,90,100]

print(idades)

rodrigo = [1, 'Rodrigo', 28, 1.75, 80]
print(rodrigo)

type(rodrigo)
# %%
print(rodrigo[1])
print(rodrigo[3])
print(sum(idades) / len(idades))
# %%
print(min(idades))
print(max(idades))

rodrigo = [1, 
           'Rodrigo', 
           28, 
           1.75,
           80, 
           [1,2,3, 'teste'], 
           [1000,  2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
           ['analista', 'desenvolvedor', 'data','gerente', 'diretor']]
print(rodrigo[5][3])
print(rodrigo[5][-1])

print(rodrigo[0:4])
# %%
print(rodrigo[6][3:])
# %%
salarios = rodrigo[6]
salarios[::2]