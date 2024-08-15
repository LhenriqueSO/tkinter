import customtkinter as ctk

janela = ctk.CTk() #Crias janela

janela._set_appearance_mode('dark') #Tema

janela.geometry("700x400") #Tamanho da tela inicial

janela.title("Agenda Digital") #Titulo do Sistema

janela.maxsize(width=900, height=550) #Tamanho maximo da janela

janela.minsize(width=500, height=300) #tamanho minimo da janela

janela.resizable(width=True, height=False) #permitir a abertura da largura ou altura, pode bloquear a mudança de tamanho


#Abas
tabview = ctk.CTkTabview(janela,width=400,corner_radius=20,border_width=1, border_color="red", fg_color="teal", segmented_button_selected_hover_color='white',segmented_button_unselected_color='blue', segmented_button_fg_color='yellow', segmented_button_selected_color='pink', segmented_button_unselected_hover_color='orange',bg_color='orange')

tabview.pack()

tabview.add('Nomes')
tabview.add('Idades')
tabview.add('Genero')

tabview.tab('Nomes').grid_columnconfigure(0,weight=1,)
tabview.tab('Idades').grid_columnconfigure(0,weight=1)
tabview.tab('Genero').grid_columnconfigure(0,weight=1)

#adicionar elemento na tab

text = ctk.CTkTabview(tabview.tab('Nomes'))

text.pack()

janela.mainloop() #Janela

