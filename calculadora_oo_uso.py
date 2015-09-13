from unittest.case import TestCase
from calculadora_oo import Operacao, CalculadoraPrefixa


class Multiplicao():
    def calcular(self, arg1, arg2):
        return arg1 * arg2


multiplicao = Multiplicao()


# class MultiplicasTests(TestCase):
#     def test_calcular(self):
#         resultado=multiplicao.calcular(2,3)
#         self.assertEqual(6,resultado)



calculadora = CalculadoraPrefixa()
calculadora.adicionar_operacao('*', multiplicao)

# print(calculadora.executar_operacao('*', 2, 3))
# print(calculadora.executar_operacao('+', 2, 3))
# print(calculadora.executar_operacao('-', 2, 3))


class Resto(Operacao):
    def calcular(self, arg1, arg2):
        return arg1 % arg2


resto = Resto()

calculadora.adicionar_operacao('%', resto)

print(calculadora.executar_operacao('%', 3, 2))

# calculadora.calcular_com_inputs()
