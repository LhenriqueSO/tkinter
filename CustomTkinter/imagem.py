import customtkinter as ctk
from PIL import Image #trabalhar com imagem

janela =ctk.CTk() #criando janela

janela.title('app teste') #colocando titulo

# janela._set_appearance_mode('dark') #Tema ligth, dark, system

janela.geometry('700x400') #dimensão inicial da janela

ctk.CTkLabel(janela,text='curso de custom tkinter - Aula-13 (Label)', font=('arial bold',20)).pack(pady=20, padx=5)


#Imagem
img1 = ctk.CTkImage(light_image=Image.open('./img.png'), size=(250,250))



ctk.CTkLabel(janela,
            text=None,
        #   hover_color='red',
            width=220,
            state='normal', #estado do botão, clicavel ou não.
            image=img1, #imagem no botão
            fg_color='transparent',
        #   command= nova_janela, #chamar uma função
            height=220,
             ).pack(pady=30)


# ctk.CTkButton(janela,
#               text="YouTube",
#             #   hover_color='red',
#               width=220,
#               height=220,
#               state='normal', #estado do botão, clicavel ou não.
#               image=img, #imagem no botão
#               fg_color='transparent',
#               command= nova_janela, #chamar uma função
#               ).pack(pady=30)





janela.mainloop()