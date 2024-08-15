import customtkinter as ctk
from PIL import Image

janela =ctk.CTk() #criando janela

janela.title('app teste') #colocando titulo

# janela._set_appearance_mode('dark') #Tema ligth, dark, system

janela.geometry('700x400') #dimensão inicial da janela

ctk.CTkLabel(janela,text='curso de custom tkinter - Aula-10 (Label)', font=('arial bold',20)).pack(pady=20, padx=5)





#Buttom
def evento():
    print('O botão foi clicaco!')

#exemplo abrir nova janela com o botão
def nova_janela():
    n_janela = ctk.CTkToplevel(janela,fg_color='teal')
    n_janela.geometry('600x300')

#colocar imagem no botão
img =ctk.CTkImage(light_image=Image.open('./img.png'), size=(200, 200))

ctk.CTkButton(janela,
              text="YouTube",
            #   hover_color='red',
              width=220,
              height=220,
              state='normal', #estado do botão, clicavel ou não.
              image=img, #imagem no botão
              fg_color='transparent',
              command= nova_janela, #chamar uma função
              ).pack(pady=30)





janela.mainloop()