# main.py
import tkinter as tk
from tkinter import ttk, Toplevel, Label, Entry, messagebox, Button, Tk
from src.vista.vista_principal import MainView



ventana = Tk()
ventana.config(bg='black')
ventana.geometry('250x250')
ventana.title('Ventana inicial')
ventana.minsize(width=250, height=250)

def abrir_vistaPrincipal():
    #ventana.destroy()
    MainView(ventana)

texto1 = Label(ventana, text='Nombre', bg='black', fg='magenta', font=('Arial',12,'bold'))
texto1.grid(row=1, column=0, padx=5, pady=5)
        
texto2 = Label(ventana, text='Apellidos', bg='black', fg='magenta', font=('Arial',12,'bold'))
texto2.grid(row=2, column=0, padx=5, pady=5)
        
texto2 = Label(ventana, text='Telefono', bg='black', fg='magenta', font=('Arial',12,'bold'))
texto2.grid(row=3, column=0, padx=5, pady=5)
        
texto3 = Label(ventana, text='Email', bg='black', fg='magenta', font=('Arial',12,'bold'))
texto3.grid(row=4, column=0, padx=5, pady=5)
        
btn_registrar = Button(ventana, text='Registrar',bg='blue',fg='magenta',font=('Arial',12,'bold'), command=abrir_vistaPrincipal)
btn_registrar.grid(row=5, column=2,padx=10, pady=10)

ventana.mainloop()
