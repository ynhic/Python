from biblioteca import *

nome1 = gera_nome_convite('henrique fernandes')

nome2 = gera_nome_convite('yngrid wasik')

print('O codigo gerado foi {} e {}'.format(nome1, nome2))

envia_convite(nome1)

envia_convite(nome2)

nome1 = processa_convite('henrique fernandes')


