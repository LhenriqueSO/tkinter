import customtkinter as ctk

janela = ctk.CTk() #Crias janela

janela._set_appearance_mode('dark') #Tema

janela.geometry("700x400") #Tamanho da tela inicial

janela.title("Agenda Digital") #Titulo do Sistema

janela.maxsize(width=900, height=550) #Tamanho maximo da janela

janela.minsize(width=500, height=300) #tamanho minimo da janela

janela.resizable(width=True, height=False) #permitir a abertura da largura ou altura, pode bloquear a mudança de tamanho


#Frame
frame1 = ctk.CTkFrame(master= janela, width=200, height=330,fg_color='teal', bg_color='red',border_width=10, border_color='green', corner_radius=30).place(x=10, y=60)

frame2 = ctk.CTkFrame(janela,width=200, height=330,fg_color='green').place(x=230, y=60)

frame3 = ctk.CTkFrame(janela, width=200, height=330, fg_color='white').place(x=450, y= 60)


janela.mainloop() #Janela

