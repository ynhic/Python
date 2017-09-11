# -*- coding: UTF-8 -*-


class Pessoa(object):
    'classe pessoa para ser usada no calculo de IMC'

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imprimi_imc(self):
        imc = self.peso/(self.altura * self.altura)
        print('o IMC para o(a) {} é de {}'.format(self.nome, imc))
