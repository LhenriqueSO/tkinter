import customtkinter as ctk

janela = ctk.CTk() #Crias janela

janela._set_appearance_mode('dark') #Tema

janela.geometry("700x400") #Tamanho da tela inicial

janela.title("Agenda Digital") #Titulo do Sistema

janela.maxsize(width=900, height=550) #Tamanho maximo da janela

janela.minsize(width=500, height=300) #tamanho minimo da janela

janela.resizable(width=True, height=False) #permitir a abertura da largura ou altura, pode bloquear a mudança de tamanho

#Multiplas janelas
def nova_janela():
    n_janela = ctk.CTkToplevel(janela,fg_color='teal')
    n_janela.geometry('600x300')

btn_novajanela = ctk.CTkButton(master=janela, text= 'Abrir nova janela', command=nova_janela).place(x=300, y=100) #Botão



janela.mainloop() #Janela

