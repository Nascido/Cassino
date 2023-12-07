
from games import Player
from interface import Casino

"""
    Cassino Royal
"""
users = []

with open('players.txt', 'r') as file:
    for line in file:
        nome, senha, fichas = line.strip().split(' - ')
        usr = Player(nome, senha, int(fichas))
        users.append(usr)

cassino = Casino(users)
cassino.login()
