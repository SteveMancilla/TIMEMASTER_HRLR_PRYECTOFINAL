#vista_principal
import tkinter as tk
from tkinter import messagebox, Label, ttk, Button, Frame, Canvas, LAST, Toplevel
from pygame import mixer
from time import strftime
from src.modelo.alarma import AlarmaApp
from src.modelo.cronometro import CronometroApp
from math import cos, sin, radians, pi

class MainView:
    def __init__(self, master):
        self.master = master
        self.ventana = Toplevel(self.master)
        self.ventana.config(bg='black')
        self.ventana.geometry('700x700')
        self.ventana.title('Trabajo Final')
        mixer.init()
        
        self.texto1 = Label(self.ventana, text='Proyecto de Fin de Curso', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        self.texto1.grid(row=1, column=0, padx=10, pady=5)

        self.texto_hora = Label(self.ventana, fg='aqua', bg='black')
        self.texto_hora.grid(row=1, column=0, columnspan=3, sticky="nsew", ipadx=5, ipady=20)
        self.obtener_tiempo()

        self.button_frame = tk.Frame(self.ventana, bg='black')
        self.button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        self.timer_button = Button(self.button_frame, text='Timer', relief="raised", bd=5, bg='green', font=('Arial',12,'bold'), width=20, command=self.abrir_cronometro)
        self.timer_button.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')

        self.alarma_button = Button(self.button_frame, text='Alarma', relief="raised", bd=5, bg='blue', font=('Arial',12,'bold'), width=20, command=self.abrir_alarma)
        self.alarma_button.grid(column=1, row=0, padx=10, pady=10, sticky='nsew')

        self.pomodoro_button = Button(self.button_frame, text='Pomodoro', relief="raised", bd=5, bg='yellow', font=('Arial',12,'bold'), width=20)
        self.pomodoro_button.grid(column=2, row=0, padx=10, pady=10, sticky='nsew')

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)

        self.frame = Frame(self.ventana, height=400, width=400, bg='black')
        self.frame.grid(column=0, row=3, columnspan=3, pady=20)
        self.canvas = Canvas(self.frame, bg='black', width=385, height=385, bd=10)
        self.canvas.grid(padx=5, pady=5)
        
        self.hr = 0
        self.mi = 0
        self.se = 0
        #self.actualizar_reloj()
        #self.reloj(self.hr,self.mi,self.se)
        self.tiempo()

    def centrar_ventana(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def obtener_tiempo(self):
        hora = strftime('%H:%M:%S')
        x = self.texto_hora.winfo_height()
        t = 30
        self.texto_hora.config(text=hora, font=('Radioland', t))
        self.texto_hora.after(1000, self.obtener_tiempo)

    def abrir_alarma(self):
        AlarmaApp(self.ventana)

    def abrir_cronometro(self):
        CronometroApp(self.ventana)

    def tiempo(self):
        global hr, mi, se	
        h = int(strftime('%H'))
        m = int(strftime('%M'))
        s = int(strftime('%S'))
        hr = (h/12)*360
        mi = (m/60)*360
        se = (s/60)*360
        self.reloj(hr,mi,se)
        self.canvas.after(1000,self.tiempo)

    def reloj(self, h, m, s):
        self.canvas.create_oval(50, 50, 350, 350, fill='black', outline='blue', width=6, activeoutline='skyblue', activefill='gray12')
        numeros = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]
        for i in range(len(numeros)):
            self.canvas.create_text(200 - 120 * sin(((i + 1) * 2 * pi) / 12), 200 - 120 * cos(((i + 1) * 2 * pi) / 12), text=numeros[i], font=('Arial', 12, 'bold'), fill='white')
        for y in range(60):
            self.canvas.create_text(200 - 140 * sin(((y + 1) * 2 * pi) / 60), 200 - 140 * cos(((y + 1) * 2 * pi) / 60), text='•', font=('Arial', 12, 'bold'), fill='deep sky blue')
        for x in range(12):
            self.canvas.create_text(200 - 140 * sin(((x + 1) * 2 * pi) / 12), 200 - 140 * cos(((x + 1) * 2 * pi) / 12), text='•', font=('Arial', 25, 'bold'), fill='green')
        self.canvas.create_line(200, 200, 200 + 60 * sin(radians(h)), 200 - 60 * cos(radians(h)), fill='green', width=9, arrow=LAST)
        self.canvas.create_line(200, 200, 200 + 80 * sin(radians(m)), 200 - 80 * cos(radians(m)), fill='blue2', width=6, arrow=LAST)
        self.canvas.create_line(200, 200, 200 + 120 * sin(radians(s)), 200 - 120 * cos(radians(s)), fill='red', width=3, arrow=LAST)
        self.canvas.create_oval(190, 190, 210, 210, fill='green', outline='black', width=2)

    def run(self):
        self.ventana.mainloop()