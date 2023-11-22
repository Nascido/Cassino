
import tkinter as tk


class Casino:
    def __init__(self, players):
        self.players = players
        self.caixa = 5000

    def show(self):
        firstwindow = tk.Tk()
        firstwindow.title("Cassino Royal")
        firstwindow.geometry("300x100")

        bemvindo = tk.Label(text="Bem vindo(a), selecione a opção desejada:")
        login = tk.Button(text="Entrar", command=self.login)
        cadastro = tk.Button(text="Cadastro", command=self.cadastro)

        bemvindo.pack()
        login.pack()
        cadastro.pack()

        firstwindow.mainloop()

    def login(self):
        def checklogin():
            usrname = username_entry.get()
            password = password_entry.get()
            encontrado = False

            for player in self.players:
                name = player.getname()
                if usrname == name:
                    senha = player.getsenha()
                    encontrado = True
                    if senha == password:
                        print("Usuário Autenticado")

                    else:
                        print("Senha incorreta")

            if not encontrado:
                print("Usuário Inexistente")

        # Login window
        login = tk.Tk()
        login.title("Login de Usuário")
        login.geometry("350x400")

        # widgets
        login_label = tk.Label(login, text="Autenticação")
        username_label = tk.Label(login, text="Nome")
        username_entry = tk.Entry(login)
        password_label = tk.Label(login, text="Senha")
        password_entry = tk.Entry(login, show='*')
        login_button = tk.Button(login, text='Entrar', command=checklogin)

        # Placing widgets
        login_label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        login_button.grid(row=3, column=0, columnspan=2)

        login.mainloop()

    def cadastro(self):
        def registrar():
            pass

        # Login window
        cadastro = tk.Tk()
        cadastro.title("Registro de Usuário")
        cadastro.geometry("350x400")

        # widgets
        registro_label = tk.Label(cadastro, text="Registro")
        cpf_label = tk.Label(cadastro, text='CPF')
        cpf_entry = tk.Entry(cadastro)
        username_label = tk.Label(cadastro, text="Nome")
        username_entry = tk.Entry(cadastro)
        password_label = tk.Label(cadastro, text="Senha")
        password_entry = tk.Entry(cadastro, show='*')
        repeat_label = tk.Label(cadastro, text="Senha")
        repeat_entry = tk.Entry(cadastro, show='*')
        login_button = tk.Button(cadastro, text='Entrar', command=registrar)

        # Placing widgets
        registro_label.grid(row=0, column=0, columnspan=2)
        cpf_label.grid(row=1, column=0)
        cpf_entry.grid(row=1, column=1)
        username_label.grid(row=2, column=0)
        username_entry.grid(row=2, column=1)
        password_label.grid(row=3, column=0)
        password_entry.grid(row=3, column=1)
        repeat_label.grid(row=4, column=0)
        repeat_entry.grid(row=4, column=1)
        login_button.grid(row=5, column=0, columnspan=2)

        cadastro.mainloop()
