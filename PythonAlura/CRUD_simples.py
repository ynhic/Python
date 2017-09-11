# -*- coding: UTF-8 -*-
import re


def cadastrar_nomes(nomes):
    nome_aux = input('digite um nome: \n')
    nomes.append(nome_aux)
    print(nomes)
    return nomes


def deletar_nomes(nomes):
    print(nomes)
    nome_aux = input('qual nome deseja remover: \n')
    nomes.remove(nome_aux)
    return nomes


def listar_nomes(nomes):
    print('Listando nomes: \n')
    for nome in nomes:
        print(nome)


def alterar_nomes(nomes):
    nome = input('Digite o nome que deseja alterar: \n')
    existe = nome in nomes

    if existe:
        nome_alterado = input('Digite o nome alterado: \n')
        index = nomes.index(nome)
        nomes[index] = nome_alterado

    else:
        print('Nome nao encontrado!')
        menu()


def procurar(nomes):
    nome = input('Digite o nome a ser procurado: \n')
    if nome in nomes:
        print('nome {} encontrado'.format(nome))
    else:
        print('nome {} nao encontrado'.format(nome))


def procurar_regex(nomes):
    exp_regular = input('Digite a expressao regular: \n')
    nome_concatenados = ' '.join(nomes)
    resultados = re.findall(exp_regular, nome_concatenados)
    print(resultados)


def menu():
    nomes = []
    escolha = ''
    while escolha != '0':
        escolha = input('1 para cadastrar, 2 para deletar, 3 para listar nomes, '
                        '4 para alterar, 5 para procurar, 6 para busca regex e  0 para terminar: \n')
        if escolha == '1':
            cadastrar_nomes(nomes)

        if escolha == '2':
            deletar_nomes(nomes)

        if escolha == '3':
            listar_nomes(nomes)

        if escolha == '4':
            alterar_nomes(nomes)
        if escolha == '5':
            procurar(nomes)
        if escolha == '6':
            procurar_regex(nomes)


menu()


#aux = int(10)
#nomes = []
#while(int(aux) != 0):
#    aux = input('1 para cadastrar ou 2 para deletar')
#
#
#   if int(aux) == 1:
#        nomes = cadastrar_nomes(nomes)
#
#    if int(aux) == 2:
#        nomes = deletar_nomes(nomes)

