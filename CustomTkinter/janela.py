import customtkinter as ctk

janela = ctk.CTk() #Crias janela

janela._set_appearance_mode('dark') #Tema

janela.geometry("700x400") #Tamanho da tela inicial

janela.title("Agenda Digital") #Titulo do Sistema

janela.maxsize(width=900, height=550) #Tamanho maximo da janela

janela.minsize(width=500, height=300) #tamanho minimo da janela

janela.resizable(width=True, height=False) #permitir a abertura da largura ou altura, pode bloquear a mudança de tamanho


janela.iconify() #Fecha a aplicação

janela.deiconify()  #Fecha a aplicação



btn = ctk.CTkButton(janela, text= 'Olá') #Botão

btn.pack() #mostrar

janela.mainloop() #Janela

