#%%
m = 1  # Começa do 1

while m <= 10:  # Loop externo para os números de 1 a 10
    print(f'Tabuada do {m}:')
    count = 1  # Reinicia o contador a cada novo número
    while count <= 10:  # Loop interno para multiplicar de 1 a 10
        print(f'{count} x {m} = {m * count}')
        count += 1  # Incrementa o multiplicador
    print('-' * 20)  # Separador entre tabuadas
    m += 1  # Passa para o próximo número

print('Fim da tabuada!')