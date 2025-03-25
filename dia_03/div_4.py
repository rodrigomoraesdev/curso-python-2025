#%%

count = 4

while count <=100:
    resto = count % 4
    if resto == 0:
        print(count)
    count += 1

#%%
count = 4
for i in range(4,101):
    if i % 4 == 0:
        print(i)