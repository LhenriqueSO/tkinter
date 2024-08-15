import customtkinter as ctk

janela = ctk.CTk() #Crias janela

# janela._set_appearance_mode() #Tema

janela.geometry("700x400") #Tamanho da tela inicial

janela.title("Agenda Digital") #Titulo do Sistema

janela.maxsize(width=900, height=550) #Tamanho maximo da janela

janela.minsize(width=500, height=300) #tamanho minimo da janela

janela.resizable(width=True, height=False) #permitir a abertura da largura ou altura, pode bloquear a mudança de tamanho




#Menu

ctk.CTkLabel(janela, text='Menu de Opções. Aula 09', font=('arial bold',20)).pack(pady=20, padx=5)

ctk.CTkLabel(janela, text='Escolha seu ano de nascimento', font=('arial bold', 14)).pack()

#Para colocar nome no menu
mes_var = ctk.StringVar(value='Escolha o mes')

#Função para mostra mes escolhido com print
def mes_nascimento(escolha):
    print(f"O seu mes de nascimento:{escolha}")

#menu opções(usando a funçã para retornar) acrescenta(variable)
mes = ctk.CTkOptionMenu(janela, values=['jan', 'fev', 'mar', 'abr','mai','jun', 'outros...'], command=mes_nascimento, variable=mes_var, width=200, height=20,corner_radius=40, button_hover_color='teal')


mes.pack(pady= 10)






'''

#menu opções(usando a funçã para retornar)
mes = ctk.CTkOptionMenu(janela, values=['jan', 'fev', 'mar', 'abr','mai','jun', 'outros...'], command=mes_nascimento)


mes.pack(pady= 10)
#nome no menu
mes.set('Meses')

'''



janela.mainloop() #Janela

