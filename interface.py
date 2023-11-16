
import tkinter as tk
from tkinter import messagebox as mbox

window = tk.Tk()
window.title("Login Casino")
window.geometry("340x400")

def login():
    mbox.showinfo(title="User Entry", message="Você logou com sucesso!")
    

# window.configure(bg="#333333")

# Widgets
login_label = tk.Label(window, text="Login")

name_label = tk.Label(window, text="Nome")
name_entry = tk.Entry(window)

password_label = tk.Label(window, text="Senha")
password_entry = tk.Entry(window, show='*')

login_button = tk.Button(window, text="Entrar", command=login)

# Placing Widgets
login_label.grid(row=0, column=0, columnspan=2)

name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)

password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)

login_button.grid(row=3, column=0, columnspan=2)

window.mainloop()
