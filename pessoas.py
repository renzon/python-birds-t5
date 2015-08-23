class Pessoa():
    olhos = 2

    def __init__(self, idade=18):
        self.idade = idade

    def cumprimentar(self, nome):
        return 'Olá sou o %s, eu tenho %s anos de idade' % (nome, self.idade)


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

Pessoa.olhos = 3
print(renzo.olhos)
print(osmar.olhos)
print(Pessoa.olhos)
print(id(renzo.olhos))
print(id(osmar.olhos))
print(id(Pessoa.olhos))

# print(Pessoa.cumprimentar(renzo))
renzo.idade = 18
print(renzo.cumprimentar(nome='Renzo'))
print(osmar.cumprimentar('Osmar'))
