import tkinter as tk
import sqlite3

# Criação da janela principal
janela = tk.Tk()
janela.title("Olá, Tkinter!")
janela.geometry("800x600+500+250")
janela.resizable(True,False)

# Rótulos simples
label = tk.Label(janela, text = "Bem-vindo ao Tkinter!")
label2 = tk.Label(janela, text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis convallis nisi. Nam et dui lobortis, tempus purus et, facilisis eros. ")
label.pack()
label2.pack()

# Início do loop principal
janela.mainloop()
