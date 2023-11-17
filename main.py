
from games import Player, Blackjack

"""
    Cassino Royal
"""

player1 = Player("Rafael", 1000, 1234)
player2 = Player("Éric", 1000, 1234)
player3 = Player("Carioca", 1000, 1234)

players = [player1, player2, player3]

game = Blackjack(players)
