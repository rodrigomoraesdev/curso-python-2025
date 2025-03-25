#%%
saldo_total = 0
while True:
    saldo = input('Digite o saldo da conta: ')
    if saldo == '':
        break   
    saldo_total += float(saldo)

print(saldo_total)
