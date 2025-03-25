#%%
idades = []

while True:
    idade = input("Digite a idade da pessoa: ")
    if idade == "":
        break
    idades.append(int(idade))
print(idades)
print('Média:', sum(idades)/len(idades))
print('Maior:', max(idades))
print('Menor:', min(idades))
print('Quantidade:', len(idades))