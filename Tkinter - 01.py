from tkinter import *

app = Tk()
app.title("ShantyTown")
app.geometry("500x400")
app.configure(background='#0ff')

txt1 = Label(app, text="Cydonia - X", foreground='#5F9EA0')
txt1.place(x= 10, y = 10, width= 150, height= 30)

valor_txt = 'Módulo Cydonia'
valor_bg = '#fff'
valor_vfg = '#5F9EA0'
txt2 = Label(text = valor_txt, bg = valor_bg, fg = valor_vfg)
txt2.pack(ipadx = 20, ipady = 20, padx = 5, pady = 5, side="top", fill=X, expand=True)

app.mainloop()              