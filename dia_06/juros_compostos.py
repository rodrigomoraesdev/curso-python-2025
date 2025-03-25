#%%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    '''
    Juros compostos servem para calcular o retorno 
    financeiro apartir de um aporte

    aporte: um numero em reais

    taxa: um numero decimal

    anos: um numero inteiro

    '''
    return aporte * (1 + taxa) ** anos

juros_compostos(aporte=1000, taxa=0.13, anos=4)

