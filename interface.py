
import tkinter as tk
# from tkinter import messagebox as mbox

from games import Blackjack


class Casino:
    def __init__(self, players):
        self.players = players
        self.caixa = 5000

    def show(self):
        root = tk.Tk()
        root.title("Cassino Royal")
        root.geometry("300x100")

        bemvindo = tk.Label(text="Bem vindo(a), selecione a opção desejada:")
        login = tk.Button(text="Login")
        cadastro = tk.Button(text="Cadastro")

        bemvindo.pack()
        login.pack()
        cadastro.pack()

        root.mainloop()

    def iniciarBlackjack(self):
        blackjackGame = Blackjack(self.players, self.caixa)

        blackjackGame.iniciar()
