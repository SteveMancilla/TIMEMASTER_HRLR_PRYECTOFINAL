from tkinter import messagebox, Label, Tk, ttk, Toplevel
from time import strftime
from pygame import mixer

class AlarmaApp:
    def __init__(self, master):
        #self.ventana = Tk()
        self.master = master
        self.ventana = Toplevel(self.master)
        self.ventana.config(bg='black')
        self.ventana.geometry('500x250')
        self.ventana.title('Alarma')
        self.ventana.minsize(width=500, height=250)
        mixer.init()

        self.lista_horas = [i for i in range(24)]
        self.lista_minutos = [i for i in range(60)]
        self.lista_segundos = [i for i in range(60)]

        self.create_widgets()
        self.obtener_tiempo()

    def create_widgets(self):
        texto1 = Label(self.ventana, text='Hora', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        texto1.grid(row=1, column=0, padx=5, pady=5)
        texto2 = Label(self.ventana, text='Minutos', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        texto2.grid(row=1, column=1, padx=5, pady=5)
        texto3 = Label(self.ventana, text='Segundos', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        texto3.grid(row=1, column=2, padx=5, pady=5)

        self.combobox1 = ttk.Combobox(self.ventana, values=self.lista_horas, style="TCombobox", justify='center', width='12', font='Arial')
        self.combobox1.grid(row=2, column=0, padx=15, pady=5)
        self.combobox1.current(0)
        self.combobox2 = ttk.Combobox(self.ventana, values=self.lista_minutos, style="TCombobox", justify='center', width='12', font='Arial')
        self.combobox2.grid(row=2, column=1, padx=15, pady=5)
        self.combobox2.current(0)
        self.combobox3 = ttk.Combobox(self.ventana, values=self.lista_segundos, style="TCombobox", justify='center', width='12', font='Arial')
        self.combobox3.grid(row=2, column=2, padx=15, pady=5)
        self.combobox3.current(0)

        style = ttk.Style()
        style.theme_create('combostyle', parent='alt', settings={'TCombobox': {'configure': {'selectbackground': 'red', 'fieldbackground': 'gold', 'background': 'blue'}}})
        style.theme_use('combostyle')

        self.ventana.option_add('*TCombobox*Listbox*Background', 'white')
        self.ventana.option_add('*TCombobox*Listbox*Foreground', 'black')
        self.ventana.option_add('*TCombobox*Listbox*selectBackground', 'green2')
        self.ventana.option_add('*TCombobox*Listbox*selectForeground', 'black')

        self.alarma_label = Label(self.ventana, fg='violet', bg='black', font=('Radioland', 20))
        self.alarma_label.grid(column=0, row=3, sticky="nsew", ipadx=5, ipady=20)
        repetir = Label(self.ventana, fg='white', bg='black', text='Repetir', font='Arial')
        repetir.grid(column=1, row=3, ipadx=5, ipady=20)
        self.cantidad = ttk.Combobox(self.ventana, values=(1, 2, 3, 4, 5), justify='center', width='8', font='Arial')
        self.cantidad.grid(row=3, column=2, padx=5, pady=5)
        self.cantidad.current(0)

        self.texto_hora = Label(self.ventana, fg='green2', bg='black')
        self.texto_hora.grid(columnspan=3, row=0, sticky="nsew", ipadx=5, ipady=20)

    def obtener_tiempo(self):
        x_hora = self.combobox1.get()
        x_minutos = self.combobox2.get()
        x_segundos = self.combobox3.get()
        hora = strftime('%H')
        minutos = strftime('%M')
        segundos = strftime('%S')
        hora_total = (hora + ' : ' + minutos + ' : ' + segundos)
        self.texto_hora.config(text=hora_total, font=('Radioland', 25))
        hora_alarma = x_hora + ' : ' + x_minutos + ' : ' + x_segundos
        self.alarma_label['text'] = hora_alarma
        # Condición:
        if int(hora) == int(x_hora) and int(minutos) == int(x_minutos) and int(segundos) == int(x_segundos):
            mixer.music.load("sound.mp3")
            mixer.music.play(loops=int(self.cantidad.get()))
            messagebox.showinfo(message=hora_alarma, title="Alarma")
        self.texto_hora.after(100, self.obtener_tiempo)

    def run(self):
        self.ventana.mainloop()