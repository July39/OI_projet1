from tkinter import *


def fermer():
    pass
def cmd_on():
    pass
def cmd_off():
    pass
def afficherHistorique():
    pass




fen1 = Tk()
fen1.protocol("WM_DELETE_WINDOW", fermer)
fen1.title("Console de controle")

lblEtat = Label(fen1, text="Alarme", fg='black', font="Helvetica 20 bold")
lblEtat.grid(row = 0, column = 0, columnspan = 2)

btn1 = Button(fen1, text='ON', fg='green', font="Helvetica 20 bold", command = cmd_on)
btn1.grid(row = 1, column = 0)

btn2 = Button(fen1, text='OFF',fg='red', font="Helvetica 20 bold", command = cmd_off)
btn2.grid(row = 1, column = 1)

lblEtat = Label(fen1, text="Lumiere entrée", fg='black', font="Helvetica 20 bold")
lblEtat.grid(row = 2, column = 0, columnspan = 2)

btn3 = Button(fen1, text='ON',fg='green', font="Helvetica 20 bold", command = cmd_on)
btn3.grid(row = 3, column = 0)

btn4 = Button(fen1, text='OFF',fg='red', font="Helvetica 20 bold", command = cmd_off)
btn4.grid(row = 3, column = 1)

lblEtat = Label(fen1, text="Smartplug", fg='black', font="Helvetica 20 bold")
lblEtat.grid(row = 4, column = 0, columnspan = 2)

btn5 = Button(fen1, text='ON',fg='green', font="Helvetica 20 bold", command = cmd_on)
btn5.grid(row = 5, column = 0)

btn6 = Button(fen1, text='OFF',fg='red', font="Helvetica 20 bold", command = cmd_off)
btn6.grid(row = 5, column = 1)

lblEtat = Label(fen1, text="Historique", fg='black', font="Helvetica 20 bold")
lblEtat.grid(row = 6, column = 0, columnspan = 2)

btn6 = Button(fen1, text='Afficher',fg='blue', font="Helvetica 20 bold", command = afficherHistorique)
btn6.grid(row = 7, column = 0)

fen1.mainloop()


def historique():
    fen2= Tk()
    fen2.title("Historique")

    resultat = Text(fen2)
    resultat.config(width = 40, height = 10, font="Helvetica")
    resultat.insert(INSERT, "" )
    resultat.insert(INSERT, "")
    resultat.insert(INSERT, "")

    resultat.grid(row = 0, column = 0, columnspan = 3)
    Button(fen2, text = "Quitter", font="Helvetica 15", command =afficherHistorique)

    fen2.mainloop()



