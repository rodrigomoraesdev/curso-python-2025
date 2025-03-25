#%%
dados = {}

while True:
    frase = input("Digite uma frase: ")
    if frase == "":
        break
    elif frase in dados:
        dados[frase] += 1
    else:
        dados[frase] = 1

ordem = list(dados.items())
ordem.sort(key=lambda x: x[-1], reverse=True)

for frase, quantidade in ordem:
    print(f'{frase}: {quantidade} vezes')