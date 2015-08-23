def calcular():
    argumento1 = float(input('Digito o primeiro parametro: '))
    sinal = input('Sinal da operação: ')
    argumento2 = float(input('Digito o segundo parametro: '))
    if sinal == '+':
        return argumento1 + argumento2
    elif sinal == '-':
        return argumento1 - argumento2
    else:
        raise Exception('Operação não suportada')
