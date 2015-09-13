lista = range(1, 10)

i = 0


# while i<= len(lista):
#     print(i, lista[i])
#     i+=1
#     # if i==5:
#     break

# for i, valor in enumerate(lista):
#     print(i, valor)

def soma(a, b, *args):

    soma = a + b
    for e in args:
        soma += e
    return soma


print(soma(1, 3))
print(soma(1, 3, 1))
print(soma(1, 3, 1, 4))

lista= [1, 2, 3]
print(soma(*lista))
