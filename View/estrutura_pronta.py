from pathlib import Path
from sys import path as s


# DEIXANDO ESTRUTURA, PRONTA PARA CASO PRECISE IMPORTAR MODULOS

caminho_atual = Path(__file__).resolve().parent

caminho = 'aqui caminho'

print(f'AQUI COMECO {caminho_atual}, {caminho}')

caminho_control = caminho_atual.parent / 'Control'

print(f'COMECO DO SEGUNDO CAMINHO  {caminho_control} {type(caminho_control)}')


s.append(str(caminho_control.resolve()))


import kaka


tunico = 'xulo'

