import customtkinter as ctk

janela = ctk.CTk() #Crias janela

janela._set_appearance_mode('dark') #Tema ligth, dark, system

janela.geometry("700x400") #Tamanho da tela inicial

janela.title("Agenda Digital") #Titulo do Sistema

janela.maxsize(width=900, height=550) #Tamanho maximo da janela

janela.minsize(width=500, height=300) #tamanho minimo da janela

janela.resizable(width=True, height=False) #permitir a abertura da largura ou altura, pode bloquear a mudança de tamanho




janela.mainloop() #Janela

