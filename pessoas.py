class Pessoa():
    olhos = 2

    def __init__(self, idade=18):
        self.idade = idade

    def cumprimentar(self, nome):
        return 'Olá sou o %s, eu tenho %s anos de idade' % (nome, self.idade)


class Homem(Pessoa):
    def cumprimentar(self, nome):
        msg = super().cumprimentar(nome)
        return 'Aperto de mão. %s' % msg
class Mulher(Pessoa):
    def cumprimentar(self, nome):
        msg = super().cumprimentar(nome)
        return 'Três beijos. %s' % msg


renzo = Homem(32)
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

mulher=Mulher()
print(mulher.cumprimentar('Marli'))
