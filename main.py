# main.py
import tkinter as tk
from tkinter import ttk, Toplevel, Label, Entry, messagebox, Button, Tk
from src.vista.vista_principal import MainView

ventana = Tk()
ventana.config(bg='black')
ventana.geometry('400x250')
ventana.title('Ventana inicial')
ventana.minsize(width=250, height=250)

def abrir_vistaPrincipal():
    #ventana.destroy()
    MainView(ventana)

nombre = Label(ventana, text='Nombre', bg='black', fg='magenta', font=('Arial',12,'bold'))
nombre.grid(row=1, column=0, padx=5, pady=5)
        
apellidos = Label(ventana, text='Apellidos', bg='black', fg='magenta', font=('Arial',12,'bold'))
apellidos.grid(row=2, column=0, padx=5, pady=5)
        
telefono = Label(ventana, text='Telefono', bg='black', fg='magenta', font=('Arial',12,'bold'))
telefono.grid(row=3, column=0, padx=5, pady=5)
        
email = Label(ventana, text='Email', bg='black', fg='magenta', font=('Arial',12,'bold'))
email.grid(row=4, column=0, padx=5, pady=5)
        
btn_registrar = Button(ventana, text='Registrar',bg='blue',fg='sky blue',font=('Arial',12,'bold'), command=abrir_vistaPrincipal)
btn_registrar.grid(row=5, column=2,padx=10, pady=10)

IngresoNombre = Entry(ventana, bg='white', fg='green', font=('Arial',12,'bold'))
IngresoNombre.grid(row=1, column=1, padx=5, pady=5)

IngresoApellidos = Entry(ventana, bg='white', fg='green', font=('Arial',12,'bold'))
IngresoApellidos.grid(row=2, column=1, padx=5, pady=5)

IngresoTelefono = Entry(ventana, bg='white', fg='green', font=('Arial',12,'bold'))
IngresoTelefono.grid(row=3, column=1, padx=5, pady=5)

IngresoEmail = Entry(ventana, bg='white', fg='green', font=('Arial',12,'bold'))
IngresoEmail.grid(row=4, column=1, padx=5, pady=5)

ventana.mainloop()