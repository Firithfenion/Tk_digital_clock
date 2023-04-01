from tkinter import *
# from tkinter.ttk import *

from time import strftime

fenster = Tk()
fenster.title("Meine Digitaluhr")
fenster.resizable(width=False, height=False)


def time():
    string2 = strftime("%d.%m.%Y")
    string = strftime('%H:%M:%S %p')
    mein_label.config(text=f"{string2}\n {string}")
    mein_label.after(1000, time)


mein_label = Label(fenster, font=('helvetica', 52), background='black', foreground='cyan')
mein_label.pack(anchor='center')

time()

mainloop()