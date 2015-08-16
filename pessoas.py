class Pessoa():
    olhos = 2

    def __init__(self, idade=18):
        self.idade = idade


renzo = Pessoa(32)
osmar = Pessoa(27)

print(type(renzo))
print(type(osmar))
print(renzo == osmar)
print(id(renzo))
print(id(osmar))
print(renzo.idade)
print(osmar.idade)
print(renzo.idade)


Pessoa.olhos=3
print(renzo.olhos)
print(osmar.olhos)
print(Pessoa.olhos)
print(id(renzo.olhos))
print(id(osmar.olhos))
print(id(Pessoa.olhos))

