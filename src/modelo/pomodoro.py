from tkinter import messagebox, Label, Entry, ttk, Toplevel, Button
from time import strftime
from pygame import mixer

class Pomodoro:
    def __init__(self, master):
        self.master = master
        self.ventana = Toplevel(self.master)
        self.ventana.config(bg='black')
        self.ventana.geometry('550x250')
        self.ventana.title('Pomodoro')
        self.ventana.minsize(width=500, height=250)
        mixer.init()

        self.create_widgets()

        self.texto_hora = Label(self.ventana, fg='aqua', bg='black')
        self.texto_hora.grid(row=1, column=0, columnspan=3, sticky="nsew", ipadx=5, ipady=20)
        self.obtener_tiempo()

    def create_widgets(self):
        text1= Label(self.ventana, text='Tiempo de trabajo', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        text1.grid(row=3, column=0, padx=5, pady=5)

        trabajoPomodoro= Entry(self.ventana, bg='white', fg='green', font=('Arial',12,'bold'))
        trabajoPomodoro.grid(row=3, column=1, padx=5, pady=5)

        text2= Label(self.ventana, text='Tiempo de descanso', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        text2.grid(row=4, column=0, padx=5, pady=5)

        descansoPomodoro= Entry(self.ventana, bg='white', fg='green', font=('Arial',12,'bold'))
        descansoPomodoro.grid(row=4, column=1, padx=5, pady=5)

        btnestablcerconfiguracionPomodoro= Button(self.ventana, text='Configuracion', bg='blue', fg='white', font=('Arial', 12, 'bold'))
        btnestablcerconfiguracionPomodoro.grid(row=20, column=0, padx=5, pady=5)

        btniniciarPomodoro= Button(self.ventana, text='Iniciar Trabajo', bg='blue', fg='white', font=('Arial', 12, 'bold'))
        btniniciarPomodoro.grid(row=20, column=1, padx=5, pady=5)

        btniniciarPeriodoTrabajoPomodoro= Button(self.ventana, text='Iniciar Descanso', bg='blue', fg='white', font=('Arial', 12, 'bold'))
        btniniciarPeriodoTrabajoPomodoro.grid(row=20, column=2, padx=5, pady=5)


    def obtener_tiempo(self):
        hora = strftime('%H:%M:%S')
        x = self.texto_hora.winfo_height()
        t = 30
        self.texto_hora.config(text=hora, font=('Radioland', t))
        self.texto_hora.after(1000, self.obtener_tiempo)

    def run(self):
        self.ventana.mainloop()