import customtkinter as ctk
from tkinter import *
janela =ctk.CTk() #criando janela

janela.title('app teste') #colocando titulo

# janela._set_appearance_mode('dark') #Tema ligth, dark, system

janela.geometry('700x400') #dimensão inicial da janela

ctk.CTkLabel(janela,text='curso de custom tkinter - Aula-10 (Label)', font=('arial bold',20)).pack(pady=20, padx=5)


#Input 

entry = ctk.CTkEntry(janela,
                     width=200,
                     placeholder_text='Digite seu nome completo: ', #texto informativo dentro do input 
                     
                     )

entry.pack(pady=20)


def pegar():

    print(entry.get()) # mostrar texto digitado, no terminar
    entry.delete(0, END) #apagar texto do input, precisar importar tkinter para 'END'


# def apagar_texto():

#     entry.delete(0, END) #apagar texto do input, precisar importar tkinter para 'END'

ctk.CTkButton(janela, 
              width=100, 
              text='Enviar', 
              corner_radius=10,
              command=pegar  #chamar função
              ).pack()


# ctk.CTkButton(janela, 
#               width=300, 
#               text='Pegar Texo', 
#               command=apagar_texto  #chamar função
#               ).pack()



janela.mainloop()