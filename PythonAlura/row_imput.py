from biblioteca import *


data_nasc = input('Digite o ano do seu nascimento: \n')
data_atual = input('Digite o ano atual: \n')

idade = calcula_idade(data_nasc, data_atual)
print(idade)

idade = calcula_idade_com_date(data_nasc)
print(idade)
