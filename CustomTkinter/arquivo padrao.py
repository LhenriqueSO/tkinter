import customtkinter as ctk

janela =ctk.CTk() #criando janela

janela.title('app teste') #colocando titulo

# janela._set_appearance_mode('dark') #Tema ligth, dark, system

janela.geometry('700x400') #dimensão inicial da janela

ctk.CTkLabel(janela,text='curso de custom tkinter - Aula-10 (Label)', font=('arial bold',20)).pack(pady=20, padx=5)




janela.mainloop()