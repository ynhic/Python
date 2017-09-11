# -*- coding: UTF-8 -*-

class Perfil():
    'classe padrão para perfis de usuário'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print('Nome: {}, Telefone: {}, Empresa: {}'.format(self.nome, self.telefone, self.empresa))

    def curtir(self):
        self.__curtidas += 1 # variaveis ou metodos que começam com __algumaCoisa são 'privados'

    def obter_curtidas(self):
        return self.__curtidas


class Data(object):
    'classe para aux na criação e impressao de datas'

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimir(self):
        print('A data formatada ficou assim : {}/{}/{}'.format(self.dia, self.mes, self.ano))


class Pessoa(object):
    'classe pessoa para ser usada no calculo de IMC'

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimi_imc(self):
        imc = self.peso/(self.altura * self.altura)
        print('o IMC para o(a) {} é de {}'.format(self.nome, imc))