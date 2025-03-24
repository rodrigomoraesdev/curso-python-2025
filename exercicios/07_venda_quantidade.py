#%%
print('''Bem-vindo ao sistema de vendas de garrafas de água
1 - Água Mineral Natural: R$ 1,50
2 - Água Mineral com Gás: R$ 2,50''')
produto = input('Digite o número do produto desejado: ')


conta = 0
if produto == '1':
    conta = 1.5
elif produto == '2':
    conta = 2.5

if conta == 0:
    print('Produto não encontrado, digite uma opção correta')
else:
    quantidade = input('Digite a quantidade desejada: ')
    quantidade = int(quantidade)
    total = conta * quantidade
    print(f'Quantidade solicitada:{quantidade}.Total R$', total)