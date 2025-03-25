#%%
#%%
palavra = input('Digite uma palavra: ')
letra = 'a'
count = 0  # Contador de ocorrências
i = 0  # Índice para percorrer a palavra

while i < len(palavra):  # Percorre cada caractere da palavra
    if palavra[i] == letra:
        count += 1
    i += 1  # Avança para o próximo caractere

print(f'A letra "{letra}" aparece {count} vezes na palavra "{palavra}".')
