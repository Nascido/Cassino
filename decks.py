
from random import shuffle


class Deck:
    def __init__(self, decks=1, blackjack=False):
        self.__nipes = ['ouros', 'copas', 'espadas', 'paus']
        self.__num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.__numberOfDecks = decks
        self.index = 0
        self._deck = []

        for i in range(decks):
            self.__gerarDeck(blackjack)

    def __gerarDeck(self, blackjack):
        for nipe in self.__nipes:
            for num in self.__num:
                self.append(Card(num, nipe, blackjack))

    def shuffle(self):
        shuffle(self._deck)

    def pop(self, index=0):
        return self._deck.pop(index)

    def append(self, carta):
        if type(carta) is Card:
            self._deck.append(carta)
        else:
            raise TypeError("the item type need to be Card")

    def remove(self, item):
        self._deck.remove(item)

    def insert(self, index, item):
        self._deck.insert(index, item)

    def distribuir(self, players, handsize):
        tamcards = len(players)*handsize
        tamdeck = len(self)

        if tamdeck >= tamcards:
            self.shuffle()
            for i in range(handsize):
                for player in players:
                    player.comprarCarta(self)
        else:
            raise ValueError("Número de cartas do deck insuficiente!")

    def getdeck(self):
        return self._deck
    
    # Builtins
    def __getitem__(self, item):
        return self._deck[item]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self._deck):
            result = self._deck[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __len__(self):
        return len(self._deck)

    def __int__(self):
        return self.__numberOfDecks

    def __str__(self):
        return f"{self.__numberOfDecks} deck(s)"


class Card:
    def __init__(self, tipo, nipe, blackjack=False, valor=None, altvalor=None, setalt=False):
        # Como identificar a carta
        self._tipo = tipo
        self._nipe = nipe

        # Qual o seu valor atribuido
        self._valorOriginal = valor
        self._valorAlternado = altvalor
        self._valor = None

        # Como ela está valendo
        self.__alt = setalt

        if self._valor is None:
            self.atribuirvalor(blackjack)

    def atribuirvalor(self, blackjack=False):
        valorCartaAlta = 10
        valorAlternativo = None
        if blackjack:
            match self._tipo:
                case "J":
                    valorComum = valorCartaAlta
                case "Q":
                    valorComum = valorCartaAlta
                case "K":
                    valorComum = valorCartaAlta
                case "A":
                    valorComum = valorCartaAlta
                    valorAlternativo = 1
                case _:
                    valorComum = int(self._tipo)

        else:
            match self._tipo:
                case "J":
                    valorComum = 11
                case "Q":
                    valorComum = 12
                case "K":
                    valorComum = 13
                case "A":
                    valorComum = 14
                    valorAlternativo = 1
                case _:
                    valorComum = int(self._tipo)

        self._valorOriginal = valorComum
        self._valorAlternado = valorAlternativo
        self.verifalt()

    def verifalt(self):
        if self.__alt:
            self._valor = self._valorAlternado
        else:
            self._valor = self._valorOriginal

    def shift(self):
        if self.__alt:
            self.__alt = False
            self.verifalt()
        else:
            if self._valorAlternado is not None:
                self.__alt = True
                self.verifalt()

        return self._valor

    # Getters
    def gettipo(self):
        return self._tipo

    def getnipe(self):
        return self._nipe

    def getvalorOriginal(self):
        return self._valorOriginal

    def getaltvalor(self):
        return self._valorAlternado

    # Builtins
    def __int__(self):
        return self._valor

    def __str__(self):
        return f"{self._tipo} de {self._nipe} "
