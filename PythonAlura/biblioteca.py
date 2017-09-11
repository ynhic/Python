# python/biblioteca.py
from datetime import *

def gera_nome_convite(convite):
    # convite = input('Digite um nome: \n')
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial: posicao_final]
    return parte1 + ' ' + parte2


def envia_convite(nome_formado):
    print('Enviando convite para {}'.format(nome_formado))


def processa_convite(convite):
    nome_formatado = gera_nome_convite(convite)
    envia_convite(nome_formatado)

def calcula_idade(data_nasc, data_atual):
    idade = int(data_atual) - int(data_nasc)
    return idade

def calcula_idade_com_date(data_nasc):
    data_atual = date.today().year
    idade = int(data_atual) - int(data_nasc)
    return idade


