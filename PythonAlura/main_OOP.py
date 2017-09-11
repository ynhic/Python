from models import Perfil
from models import Data
from models import Pessoa


perfil1 = Perfil('henrique', 'nao tem', 'programas')

perfil1.imprimir()
print(perfil1.obter_curtidas())

perfil1.curtir()
perfil1.curtir()
perfil1.curtir()
print(perfil1.obter_curtidas())
perfil1.curtir()
print(perfil1.obter_curtidas())

d = Data(21, 11, 2007)
d.imprimir()

pessoa1 = Pessoa(nome='henrique', peso=135, altura=1.84)
pessoa1.imprimi_imc()