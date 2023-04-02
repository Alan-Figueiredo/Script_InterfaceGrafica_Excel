from tkinter import *
import script 

i = 0
def teste():
    global i
    script.start(i)
    i += 1
    print(i)
    if(i >= 17):
        janela.destroy()

janela = Tk()
janela.geometry("300x100")
frame = Frame(janela)
frame.pack(fill=BOTH, expand=True)
botao = Button(frame, text="Next",height=100,command=teste)
botao.pack(pady=30, padx=100, ipadx=50)

janela.mainloop()
