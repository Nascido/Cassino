from decks import Deck, Card


class Game:
    def __init__(self, players) -> None:
        self._players = players
        self._pote = 0
        self._caixa = 0

    def getplayers(self):
        return self._players


class Hand:
    def __init__(self):
        self._hand = []
        self.index = 0

    def eraseHand(self):
        self._hand = []

    def sum21(self):
        soma = 0
        for carta in self._hand:
            if int(carta) == 11:
                tmp = soma
                soma += int(carta)
                if soma > 21:
                    soma = tmp + carta.shift()

            else:
                soma += int(carta)

        return soma

    # Métodos típicos de uma lista
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
            self.index = 0
            raise StopIteration

    def __len__(self):
        return len(self._hand)


class Player(Hand):
    def __init__(self, nome, cpf, senha, fichas=100):
        super().__init__()
        self._name = nome
        self._cpf = cpf
        self._senha = senha
        self._fichas = fichas

    # Métodos do Player
    def comprarCarta(self, deck):
        self._hand.append(deck.pop())

    def testeFichas(self, valor):
        return self._fichas > valor

    def apostar(self, valor):
        if self._fichas >= valor:
            self._fichas -= valor
            return valor
        else:
            raise ValueError

    def receberFichas(self, valor):
        self._fichas += valor

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

    def __str__(self):
        return f"{self._name}: {self._hand}"


class Dealer(Hand):
    def __init__(self, blackjack=False):
        super().__init__()
        self.gametype = blackjack
        self.auto = False
        self.deck = None

        if self.gametype:
            self.auto = True

    def comprarCarta(self):
        self._hand.append(self.deck.pop())

    def iniciar(self, players):
        self.deck = Deck(blackjack=self.gametype)
        self.deck.shuffle()

        for player in players:
            player.eraseHand()

        if self.auto:
            self.eraseHand()

    def distribuir(self, players, handsize=2):
        if self.deck is not None:
            self.deck.distribuir(players, handsize)

            if self.auto:
                self._hand.append(self.deck.pop())
        else:
            raise TypeError("Deck do dealer não inicializado!")

    def __str__(self):
        return f"Dealer: {self._hand}"


class Blackjack(Game):
    def __init__(self, players, caixa=10000, apostaInicial=20) -> None:
        super().__init__(players)
        self._dealer = Dealer(blackjack=True)
        self._apostaInicial = apostaInicial
        self._caixa = caixa

    def iniciar(self):
        self._dealer.iniciar(self._players)
        self._dealer.distribuir(self._players)

    def hit(self, player):
        if player.sum21() < 21:
            self._dealer.deck.givecard(player)
        else:
            raise ValueError("Valor 21 já alcançado ou estourado")

    def dealerHit(self):
        if self._dealer.sum21() < 17:
            self._dealer.comprarCarta()
            return True

        else:
            return False
