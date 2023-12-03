from tkinter import *
from tkinter import messagebox
import random

def card_clicked(col):
    global gato
    casinha=botoes[col-1]
    #print(casas)
    if col==gato:
        casinha.config(text = "MIAW!!")
        messagebox.showinfo('Fim de Jogo', 'Você achou o gato!')
        janela.quit()
    else:
        placar()
        if (gato==casa):
            casas[gato]=''
            casas[casa-1]='gato'
            gato=casa-1
        elif (gato==1):
            casas[gato]=''
            casas[2]='gato'
            gato=2
        else:
            casas[gato]=''
            gato+=random.choice([-1,1])
            casas[gato]='gato'

def placar():
    global tentativas
    tentativas += 1
    tentativas_label.config(text='Tentativas: {}'.format(tentativas))



janela = Tk()
janela.title("THE CAT's GAME")
janela.configure(bg='green')


#photo = PhotoImage(file = r"C:\Users\isabe\OneDrive\VSCFiles\Imagens")
FONT_STYLE = ('Arial', 15, 'bold')
botoes=[]
casa=5
gato=random.randint(1,casa)
casas=dict.fromkeys(list(range(1,casa+1)),'')
casas[gato]='gato'
tentativas=0


FONT_STYLE1 = ('Arial', 25, 'bold')
titulo = Label(janela, text='ENCONTRE O GATO!!', fg='black', bg='green',font=FONT_STYLE1)
titulo.grid(row=0, columnspan=casa+3, padx=10, pady=10)


for col in range(1,casa+1):
    card = Button(janela, text="Casa "+ str(col), width=10, height=5, bg='white',
                    relief=RAISED, bd=5, command=lambda c=col: card_clicked(c))
    card.grid(row=1, column=col, padx=5, pady=5)
    botoes.append(card)


tentativas_label = Label(janela, text='Tentativas: {}'.format(tentativas), fg='white', bg='green',font=FONT_STYLE)
tentativas_label.grid(row=2, columnspan=casa+3, padx=10, pady=10)

janela.mainloop()