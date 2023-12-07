
import tkinter as tk
from tkinter import messagebox as mg
from PIL import ImageTk as TkImg
# from PIL import Image
from games import Player, Blackjack


class Interface:
    def __init__(self, usuarios):
        self.users = usuarios
        self._usr = usuarios[0]

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
        global times_hitted
        times_hitted = 0

        game = Blackjack([self._usr])
        dealer = game.getdealer()
        player = self._usr
        game.iniciar()

        game_window = tk.Toplevel()
        game_window.title("Blackjack Game")
        game_window.geometry("800x500")

        sum_player = f'{player.sum21()}'

        # Commands
        def restart():
            game_window.destroy()
            self.blackjack()


        def hit():
            global times_hitted
            global sum_player_label
            global sum_player
            global card2_player
            global card3_player
            global card4_player
            global card5_player
            global hit_button

            game.hit(player)

            if times_hitted == 0:
                card2_player = TkImg.PhotoImage(player[2].display())
                card2_player_label = tk.Label(player_card_frame, image=card2_player)
                card2_player_label.grid(row=0, column=2)
                times_hitted += 1

            elif times_hitted == 1:
                card3_player = TkImg.PhotoImage(player[3].display())
                card3_player_label = tk.Label(player_card_frame, image=card3_player)
                card3_player_label.grid(row=0, column=3)
                times_hitted += 1

            elif times_hitted == 2:
                card4_player = TkImg.PhotoImage(player[4].display())
                card4_player_label = tk.Label(player_card_frame, image=card4_player)
                card4_player_label.grid(row=0, column=4)
                times_hitted += 1

            elif times_hitted == 3:
                card5_player = TkImg.PhotoImage(player[5].display())
                card5_player_label = tk.Label(player_card_frame, image=card5_player)
                card5_player_label.grid(row=0, column=5)
                times_hitted += 1

            sum_player = player.sum21()
            sum_player_label = tk.Label(game_window, text=f'{sum_player}')
            sum_player_label.place(relx=0.98, rely=0.56, relwidth=0.20, relheight=0.3, anchor='ne')

            if sum_player >= 21:
                hit_button = tk.Button(button_frame, text="HIT", state="disabled")
                hit_button.place(relx=0.60, rely=0.15)
                stay()

        def stay():
            global hit_button
            global stay_button
            global sum_dealer
            global sum_dealer_label
            global card0_dealer
            global card0_dealer_label
            global card1_dealer
            global card1_dealer_label
            global card2_dealer
            global card3_dealer
            global card4_dealer
            global card5_dealer

            card0_dealer = TkImg.PhotoImage(dealer[0].display())
            card0_dealer_label = tk.Label(dealer_card_frame, image=card0_dealer)
            card0_dealer_label.grid(row=0, column=0)

            card1_dealer = TkImg.PhotoImage(dealer[1].display())
            card1_dealer_label = tk.Label(dealer_card_frame, image=card1_dealer)
            card1_dealer_label.grid(row=0, column=1)

            sum_dealer = dealer.sum21()
            sum_dealer_label = tk.Label(game_window, text=sum_dealer)
            sum_dealer_label.place(relx=0.98, rely=0.24, relwidth=0.20, relheight=0.3, anchor='ne')

            while sum_dealer < 17:
                game.dealerhit()
                tam_dealer = len(dealer)

                for i in range(2, tam_dealer):
                    if i == 2:
                        card2_dealer = TkImg.PhotoImage(dealer[2].display())
                        card2_dealer_label = tk.Label(dealer_card_frame, image=card2_dealer)
                        card2_dealer_label.grid(row=0, column=2)

                    elif i == 3:
                        card3_dealer = TkImg.PhotoImage(dealer[3].display())
                        card3_dealer_label = tk.Label(dealer_card_frame, image=card3_dealer)
                        card3_dealer_label.grid(row=0, column=3)

                    elif i == 4:
                        card4_dealer = TkImg.PhotoImage(dealer[4].display())
                        card4_dealer_label = tk.Label(dealer_card_frame, image=card4_dealer)
                        card4_dealer_label.grid(row=0, column=4)

                    sum_dealer = dealer.sum21()
                    sum_dealer_label = tk.Label(game_window, text=sum_dealer)
                    sum_dealer_label.place(relx=0.98, rely=0.24, relwidth=0.20, relheight=0.3, anchor='ne')

            hit_button = tk.Button(button_frame, text="HIT", state="disabled")
            hit_button.place(relx=0.60, rely=0.15)

            stay_button = tk.Button(button_frame, text="STAY", state="disabled")
            stay_button.place(relx=0.30, rely=0.15)

            restart_button = tk.Button(game_window, text="RESTART", command=restart)
            restart_button.place(relx=0.93, rely=0.88, relwidth=0.10, relheight=0.08, anchor='ne')

        # Frames
        dealer_frame = tk.Frame(game_window, bg='#bdbdbd')
        dealer_card_frame = tk.Frame(dealer_frame)
        player_frame = tk.Frame(game_window, bg='#bdbdbd')
        player_card_frame = tk.Frame(player_frame)
        button_frame = tk.Frame(game_window, bg='#bdbdbd')

        # Cards Display
        # Dealer
        card0_dealer = TkImg.PhotoImage(dealer[0].display())
        card1_dealer = TkImg.PhotoImage(dealer[1].display(True))

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
        card0_dealer_label = tk.Label(dealer_card_frame, image=card0_dealer)
        card1_dealer_label = tk.Label(dealer_card_frame, image=card1_dealer)

        # Player
        card0_player_label = tk.Label(player_card_frame, image=card0_player)
        card1_player_label = tk.Label(player_card_frame, image=card1_player)

        # Sum Label

        sum_dealer = '?'
        sum_dealer_label = tk.Label(game_window, text=sum_dealer)
        sum_player_label = tk.Label(game_window, text=sum_player)

        # Buttons
        hit_button = tk.Button(button_frame, text="HIT", command=hit)
        stay_button = tk.Button(button_frame, text="STAY", command=stay)

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
        dealer_label.pack()
        dealer_card_frame.pack()
        card0_dealer_label.grid(row=0, column=0)
        card1_dealer_label.grid(row=0, column=1)

        # Placing Widgets on Player Frame
        player1_label.pack()
        player_card_frame.pack()
        card0_player_label.grid(row=0, column=0)
        card1_player_label.grid(row=0, column=1)

        # Placing Widgets on Button Frame
        hit_button.place(relx=0.60, rely=0.15)
        stay_button.place(relx=0.30, rely=0.15)

        game_window.mainloop()
