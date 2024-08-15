import customtkinter as ctk

janela =ctk.CTk() #criando janela

janela.title('app teste') #colocando titulo

# janela._set_appearance_mode('dark') #Tema ligth, dark, system

janela.geometry('700x400') #dimensão inicial da janela

ctk.CTkLabel(janela,text='curso de custom tkinter - Aula-10 (Label)', font=('arial bold',20)).pack(pady=20, padx=5)

#Texto estático
ctk.CTkLabel(janela, text='Digite seu Nome Completo').pack()


# #Testo (label) dinamico

# #Usar para ter senha no arquivo para digitar asntes de abrir
# text_var = ctk.StringVar(value=input('Digite seu nome: '))

# # 1 Introduzindo texto por input
# label = ctk.CTkLabel(janela, textvariable=text_var, width=200, height=25,text_color='red',font=('arial bold', 16)).pack()

#--------------------------------------------------------


# 2 Introduzindo texto por entry
def enviar(): #função para exibir text do input, na label
    texto = entry.get()
    label.configure(text=str(texto))
    ...

label = ctk.CTkLabel(janela,text='', width=200, height=25,text_color='red',font=('arial bold', 16))

label.pack(pady=10)

entry = ctk.CTkEntry(janela, width=200, corner_radius=10)
entry.pack()

ctk.CTkButton(janela, text='Enviar', width=200, corner_radius=10,command=enviar).pack(pady=10)


janela.mainloop()