from decks import Deck, Card


class Game:
    def __init__(self, players) -> None:
        self._players = players
        self._pote = 0
        self._caixa = 0

    def getplayers(self):
        return self._players


class Player:
    def __init__(self, nome, cpf, senha, fichas=100):
        self._name = nome
        self._cpf = cpf
        self._senha = senha
        self._hand = []
        self._fichas = fichas
        self.index = 0

    # Métodos do Player
    def comprarCarta(self, deck):
        carta = deck.pop()
        self._hand.append(carta)

    def testeFichas(self, valor):
        return self._fichas > valor

    def apostar(self, valor):
        if self._fichas >= valor:
            self._fichas -= valor
            return valor
        else:
            raise ValueError

    def receber(self, valor):
        self._fichas += valor

    def sum(self):
        soma = 0
        for carta in self._hand:
            soma += int(carta)

        return soma

    def pop(self, indexCarta=0):
        return self._hand.pop(indexCarta)

    def append(self, item):
        if type(item) is Card:
            self._hand.append(item)

        else:
            raise TypeError("the item type need to be Card")

    def remove(self, item):
        self._hand.remove(item)

    def insert(self, index, item):
        self._hand.insert(index, item)

    # Getters
    def getname(self):
        return self._name

    def getcpf(self):
        return self._cpf

    def getsenha(self):
        return self._senha

    def getfichas(self):
        return self._fichas

    def getplayerinfo(self):
        return self._name, self._cpf, self._senha, self._fichas

    # Builtins
    def __getitem__(self, item):
        return self._hand[item]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self._hand):
            result = self._hand[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __len__(self):
        return len(self._hand)

    def __int__(self):
        return sum(self)

    def __str__(self):
        return f"{self._name}"


class Blackjack(Game):
    def __init__(self, players, caixa, apostaInicial=20) -> None:
        super().__init__(players)
        self._dealer = Player("Dealer", caixa, 1234)
        self._deck = Deck(blackjack=True)
        self._apostaInicial = apostaInicial

    def iniciar(self):
        self._deck.shuffle()

        self._dealer.append(self._deck.pop())

        self._deck.distribuir(self._players, 2)

    def hit(self, player):
        if int(player) < 21:
            self._deck.givecard(player)
        else:
            raise ValueError("Valor 21 já alcançado ou estourado")

    def dealerTurn(self):
        dealer = self._dealer
        deck = self._deck

        while int(dealer) < 17:
            deck.givecard(dealer)
