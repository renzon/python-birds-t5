lista = [1, 2, 3]

print(lista[0])

for elemento in lista:
    print(lista)

for i, elemento in enumerate(lista):
    print(i, elemento)

idades={'Renzo':32, 'Osmar':27, 1: 4}

for chave, valor in idades.items():
    print(chave, valor)

print(idades['Renzo'])

print(idades[1])

dct={1:'Primo',2:'Primo', 5:'Prime'}