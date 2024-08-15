from typing import Tuple
import customtkinter as ctk
from tkinter import *

#abrir janela
class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.configuracoes_janela_inicial() #chma função ao iniciar sistema
        self.tela_login()

    #configurando Janela principal
    def configuracoes_janela_inicial(self):
        self.geometry('700x400')
        self.title('Tela de Login')
        self.wm_resizable(False, False)

    #tela
    def tela_login(self):
        #trabalhando com imagens
        self.img = PhotoImage(file="img.png") #do tkinter
        self.label_img =ctk.CTkLabel(self, text=None, image= self.img)
        self.label_img.grid(row=1, column=0, padx=10) #padx espaço de todos lados, row linha, column coluna


if __name__ == "__main__":
    app = App()
    app.mainloop()