class Operacao():
    def calcular(self, arg1, arg2):
        raise NotImplementedError('Implementar método calcular')


class Adicao(Operacao):
    def calcular(self, arg1, arg2):
        return arg1 + arg2


class Subtracao(Operacao):
    def calcular(self, arg1, arg2):
        return arg1 - arg2


class Calculadora():
    def calcular_com_inputs(self):
        raise Exception('Deve implementar as entradas de dados do usuário')

    def __init__(self):
        self.operacoes = {}
        adicao = Adicao()
        self.adicionar_operacao('+', adicao)
        subtracao = Subtracao()
        self.adicionar_operacao('-', subtracao)

    def adicionar_operacao(self, sinal, operacao):
        self.operacoes[sinal] = operacao

    def executar_operacao(self, sinal, arg1, arg2):  # sinal = +
        operacao_escolhida = self.operacoes[sinal]
        resultado = operacao_escolhida.calcular(arg1, arg2)
        return resultado


class CalculadoraInfixa(Calculadora):
    def calcular_com_inputs(self):
        argumento1 = float(input('Digito o primeiro parametro: '))
        sinal = input('Sinal da operação: ')
        argumento2 = float(input('Digito o segundo parametro: '))
        print(self.executar_operacao(sinal, argumento1, argumento2))


class CalculadoraPrefixa(Calculadora):
    def calcular_com_inputs(self):
        sinal = input('Sinal da operação: ')
        argumento1 = float(input('Digito o primeiro parametro: '))
        argumento2 = float(input('Digito o segundo parametro: '))
        print(self.executar_operacao(sinal, argumento1, argumento2))
