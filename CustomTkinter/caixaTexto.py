import customtkinter as ctk

janela = ctk.CTk() #Crias janela

janela._set_appearance_mode('dark') #Tema

janela.geometry("700x400") #Tamanho da tela inicial

janela.title("Bloco de Notas") #Titulo do Sistema

janela.maxsize(width=900, height=550) #Tamanho maximo da janela

janela.minsize(width=500, height=300) #tamanho minimo da janela

janela.resizable(width=True, height=False) #permitir a abertura da largura ou altura, pode bloquear a mudança de tamanho


#caixa de Texto
texto = ctk.CTkTextbox(janela, width=300, height=350, scrollbar_button_color='red',scrollbar_button_hover_color='orange', border_width=0.5, corner_radius=15, fg_color='teal', border_spacing=10)
texto.pack()

texto.insert('0.0', "Bloco de Notas" + "Esse é meu bloco de notas"*200)


janela.mainloop() #Janela

