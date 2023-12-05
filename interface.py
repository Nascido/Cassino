
import tkinter as tk
from tkinter import messagebox as mg
from PIL import ImageTk as TkImg
from games import Player, Blackjack


class Interface:
    def __init__(self, usuarios):
        self.users = usuarios
        self._usr = None

    def register(self):
        def saveInfo():
            username = username_entry.get()
            password = password_entry.get()
            fichas = 200
            registrado = False

            for user in self.users:
                name = user.getname()
                if username == name:
                    registrado = True
                    mg.showinfo("Usuário já cadastrado!", "Nome de Usuário já cadastrado")
                    break

            if not registrado:
                with open('players.txt', 'a') as file:
                    registro = f"\n{username} - {password} - {fichas}"
                    file.write(registro)

                self.users.append(Player(username, password, fichas))
                mg.showinfo("Cadastro", "Usuário cadastrado com Sucesso")

        # Login window
        register = tk.Tk()
        register.title("Registro de Usuário")
        register.geometry("350x250")

        # Frames
        usr = tk.Frame(register)
        senha = tk.Frame(register)

        # Widgets
        registro_label = tk.Label(register, text="Registro")
        username_label = tk.Label(usr, text="Nome")
        username_entry = tk.Entry(usr)
        password_label = tk.Label(senha, text="Senha")
        password_entry = tk.Entry(senha, show='*')
        login_button = tk.Button(register, text='Entrar', command=saveInfo)

        # Placing widgets
        registro_label.pack()

        usr.pack()
        username_label.grid(row=0, column=0)
        username_entry.grid(row=0, column=1)

        senha.pack()
        password_label.grid(row=0, column=0)
        password_entry.grid(row=0, column=1)

        login_button.pack()

        register.mainloop()

    def login(self):
        def checklogin():
            usrname = username_entry.get()
            password = password_entry.get()
            encontrado = False

            for usr in self.users:
                name = usr.getname()
                if usrname == name:
                    senha = usr.getsenha()
                    encontrado = True
                    if senha == password:
                        print("Usuário Autenticado")
                        self._usr = usr
                        self.acess()

                    else:
                        print("Senha incorreta")
                        mg.showinfo("Falha no Login", "Senha Incorreta!", icon='error')

            if not encontrado:
                print("Usuário Inexistente")
                mg.showinfo("Falha no Login", "Usuário não encontrado!", icon='error')

        # Login window
        login = tk.Tk()
        login.title("Login de Usuário")
        login.geometry("350x200")

        frame_login = tk.Frame(login)
        frame_login.pack()

        # widgets
        login_label = tk.Label(frame_login, text="Login")
        username_label = tk.Label(frame_login, text="Usuário")
        username_entry = tk.Entry(frame_login)
        password_label = tk.Label(frame_login, text="Senha")
        password_entry = tk.Entry(frame_login, show='*')
        login_button = tk.Button(frame_login, text='Entrar', command=checklogin)

        # Placing widgets
        login_label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        login_button.grid(row=3, column=0, columnspan=2)

        login.mainloop()

    def acess(self):
        nome = self._usr.getname()
        intro_usario = f"Bem vindo {nome}"

        sistem = tk.Tk()
        welcome = tk.Label(sistem, text=intro_usario)
        welcome.pack()

        sistem.mainloop()


class Casino(Interface):
    def __init__(self, players):
        super().__init__(players)
        self.caixa = 5000

    def acess(self):
        self.blackjack()

    def show(self):
        firstwindow = tk.Tk()
        firstwindow.title("Cassino Royal")
        firstwindow.geometry("300x100")

        bemvindo = tk.Label(text="Bem vindo(a), selecione a opção desejada:")
        login = tk.Button(text="Entrar", command=self.login)
        cadastro = tk.Button(text="Cadastro", command=self.register)

        bemvindo.pack()
        login.pack()
        cadastro.pack()

        firstwindow.mainloop()

    def blackjack(self):
        game = Blackjack(self.users)
        dealer = game.getdealer()
        players = game.getplayers()
        game.iniciar()

        player = players[0]

        game_window = tk.Tk()
        game_window.title("Blackjack Game")
        game_window.geometry("800x500")

        # Frames
        dealer_frame = tk.Frame(game_window, bg='#bdbdbd')
        player_frame = tk.Frame(game_window, bg='#bdbdbd')
        button_frame = tk.Frame(game_window, bg='#bdbdbd')

        # Cards Display
        # Dealer
        verso_dealer = True
        card0_dealer = TkImg.PhotoImage(dealer[1].display(verso_dealer))
        card1_dealer = TkImg.PhotoImage(dealer[0].display())

        # Player
        card0_player = TkImg.PhotoImage(player[0].display())
        card1_player = TkImg.PhotoImage(player[1].display())

        # Labels Texts
        intro_label = tk.Label(game_window, text="Blackjack", bg='#bfac88')
        hands_label = tk.Label(game_window, text="Hands", bg='#bfac88')
        sum_text_label = tk.Label(game_window, text="Sum", bg='#bfac88')
        dealer_label = tk.Label(dealer_frame, text=dealer)
        player1_label = tk.Label(player_frame, text=player, padx=20)

        # Cards Label
        # Dealer
        card0_dealer_label = tk.Label(dealer_frame, image=card1_dealer)
        card1_dealer_label = tk.Label(dealer_frame, image=card0_dealer)

        # Player
        card0_player_label = tk.Label(player_frame, image=card0_player)
        card1_player_label = tk.Label(player_frame, image=card1_player)

        # Sum Label
        if verso_dealer:
            sum_dealer = '?'

        else:
            sum_dealer = f'{dealer.sum21()}'

        sum_dealer_label = tk.Label(game_window, text=sum_dealer)

        sum_player = f'{player.sum21()}'
        sum_player_label = tk.Label(game_window, text=sum_player)

        # Placing Widgets Game Window
        intro_label.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.09)
        hands_label.place(relx=0.02, rely=0.13, relwidth=0.74, relheight=0.09)
        sum_text_label.place(relx=0.98, rely=0.13, relwidth=0.20, relheight=0.09, anchor='ne')
        dealer_frame.place(relx=0.02, rely=0.24, relwidth=0.74, relheight=0.3)
        player_frame.place(relx=0.02, rely=0.56, relwidth=0.74, relheight=0.3)
        sum_dealer_label.place(relx=0.98, rely=0.24, relwidth=0.20, relheight=0.3, anchor='ne')
        sum_player_label.place(relx=0.98, rely=0.56, relwidth=0.20, relheight=0.3, anchor='ne')
        button_frame.place(relx=0.02, rely=0.97, relwidth=0.74, relheight=0.09, anchor='sw')

        # Placing Widgets on dealer Frame
        dealer_label.grid(row=0, column=0, columnspan=2)
        card0_dealer_label.grid(row=1, column=0)
        card1_dealer_label.grid(row=1, column=1)

        # Placing Widgets on Player Frame
        player1_label.grid(row=0, column=0, columnspan=2)
        card0_player_label.grid(row=1, column=0)
        card1_player_label.grid(row=1, column=1)

        """
        # Grid Widgets Game Window
        intro_label.grid(row=0, column=0, columnspan=2)
        hands_label.grid(row=1, column=0)
        sum_text_label.grid(row=1, column=1)
        dealer_frame.grid(row=2, column=0)
        sum_dealer_label.grid(row=2, column=1)
        player_frame.grid(row=3, column=0)
        sum_player_label.grid(row=3, column=1)
        button_frame.grid(row=4, column=0, columnspan=2)
        """

        """  
        # Placing Widgets Dealer Frame
        dealer_label.grid(row=0, column=0)
        card0_dealer_label.grid(row=1, column=0)
        card1_dealer_label.grid(row=1, column=1)
        """

        """
        # Placing Widgets Player Frame
        player1_label.grid(row=0, column=0)
        card0_player_label.grid(row=1, column=0)
        card1_player_label.grid(row=1, column=1)
        """

        game_window.mainloop()
