import customtkinter as ctk

janela = ctk.CTk() #Crias janela

janela._set_appearance_mode('dark') #Tema

janela.geometry("700x400") #Tamanho da tela inicial

janela.title("Agenda Digital") #Titulo do Sistema

janela.maxsize(width=900, height=550) #Tamanho maximo da janela

janela.minsize(width=500, height=300) #tamanho minimo da janela

janela.resizable(width=True, height=False) #permitir a abertura da largura ou altura, pode bloquear a mudança de tamanho

#Função para o botão
def abrir():
    #Criando caixa de dialogo(input)
    dialogo = ctk.CTkInputDialog(title='Caixa de diálogo',text='Digite o seu Número de Celular',button_hover_color='red')

    print('Número do celular',dialogo.get_input()) #Mostra a informação que entra no input


#Multiplas janelas
btn = ctk.CTkButton(janela, text='Abrir caixa de diálogo!',command=abrir, bg_color='black')
btn.pack()

janela.mainloop() #Janela

