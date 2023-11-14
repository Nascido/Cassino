from games import Game


class Blackjack(Game):
    def __init__(self, players, caixa, apostaInicial=20) -> None:
        super().__init__(players)
        self._dealerHand = []
        self._rodadas = 0
        self._apostaInicial = apostaInicial
        self.caixa  = caixa

    def iniciar(self):
        participantes = []
        for player in self._players:
            participar = bool(input(f"{player} vai participar?"))

            if participar:
                participantes.append(player)

    def rodada(self, players):
        pass
