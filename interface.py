
import tkinter as tk
from tkinter import messagebox as mg
from games import Player


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
