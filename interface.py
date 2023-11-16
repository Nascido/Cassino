
import tkinter as tk
from tkinter import messagebox as mbox

from games import Blackjack


class Casino:
    def __init__(self, players):
        self.players = players
        self.caixa = 5000

    def show(self):
        root = tk.Tk()
        root.title("Bem Vindo(a)!")
        root.geometry("600x300")

        tk.Label(root, text="Jogos Disponíveis: ").pack()
        tk.Button(root, text="Blackjack").pack()
        tk.Button(root, text="Poker").pack()

        root.mainloop()

    def iniciarBlackjack(self):
        blackjackGame = Blackjack(self.players, self.caixa)

        blackjackGame.iniciar()
