
from games import Player
from interface import Casino
import json

"""
    Cassino Royal
"""
users = []


def obeter_usuarios(arquivo_players):
    with open(arquivo_players, 'r') as arquivo:
        dados = json.load(arquivo)

    return dados


dados_usuers = obeter_usuarios('player.json')

for usr in dados_usuers:
    nome = usr['nome']
    senha = usr['senha']
    fichas = usr['fichas']

    usuario = Player(nome, senha, fichas)

    users.append(usuario)

cassino = Casino(users)
cassino.show()
