#%%
soma = 0
qtde = 4

while qtde > 0:
    altura = input('Digite a altura: ')
    altura = float(altura)
    soma += altura
    qtde -= 1
print(soma)

#%%
soma = 0
qtde = 4

for i in range(qtde):
    altura = input('Digite a altura: ')
    altura = float(altura)
    soma += altura
print(soma)