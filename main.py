
from games import Player
from interface import Casino

"""
    Cassino Royal
"""
players = []

with open('players.txt', 'r') as file:
    for line in file:
        nome, cpf, senha, fichas = line.strip().split(' - ')
        usr = Player(nome, int(cpf), senha, int(fichas))
        players.append(usr)

cassino = Casino(players)
cassino.show()
