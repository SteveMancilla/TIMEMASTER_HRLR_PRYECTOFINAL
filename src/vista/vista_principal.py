from tkinter import messagebox, Label, Tk, ttk, Button
import tkinter as tk
from pygame import mixer
from time import strftime

ventana = Tk()
ventana.config(bg='black')
ventana.geometry('500x500')
ventana.title('Trabajo Final')

mixer.init()

texto1 = Label(ventana, text='Proyecto de Fin de Curso', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
texto1.grid(row=1, column=0, padx=100, pady=5)

def obtener_tiempo():
    hora = strftime('%H:%M:%S')
    x = texto_hora.winfo_height()
    t = int((x-5)*0.32)
    texto_hora.config(text=hora, font=('Radioland', t))
    texto_hora.after(1000, obtener_tiempo)


texto_hora = Label(ventana, fg='aqua', bg='black')
texto_hora.grid(row=3, sticky="nsew", ipadx=5, ipady=20)

timer = Button()

obtener_tiempo()
ventana.mainloop()