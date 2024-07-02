#NO BORRAR


from tkinter import Canvas, Button, Frame, Label, Tk, Toplevel
from datetime import datetime, time
from src.modelo.db import DB, TimerModel, UsuarioModel

class CronometroApp:
    def __init__(self, master):
        self.mi = 0
        self.se = 0
        self.ml = 0
        self.contar = 0
        self.click_lectura = 0
        self.clik_stop = 0
        self.clik_inicio = 0

        self.master = master
        self.ventana = Toplevel(self.master)
        #self.ventana = Tk()
        self.ventana.config(bg='black')
        self.ventana.geometry('500x250')
        self.ventana.title('Cronometro')
        self.ventana.minsize(width=500, height=250)

        self.ventana.columnconfigure([0, 1, 2], weight=2)
        self.ventana.rowconfigure(0, weight=2)
        self.ventana.rowconfigure(1, weight=1)

        self.create_frames()
        self.create_widgets()
        self.coordenadas()

    def create_frames(self):
        self.frame1 = Frame(self.ventana)
        self.frame1.grid(column=0, row=0, sticky='snew')
        self.frame2 = Frame(self.ventana)
        self.frame2.grid(column=1, row=0, sticky='snew')
        self.frame3 = Frame(self.ventana)
        self.frame3.grid(column=2, row=0, sticky='snew')
        self.frame4 = Frame(self.ventana, bg='gray10')
        self.frame4.grid(row=1, columnspan=3, sticky='snew')
        self.frame5 = Frame(self.ventana, bg='black')
        self.frame5.grid(row=2, columnspan=3, sticky='snew')

        self.frame1.columnconfigure(0, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.rowconfigure(0, weight=1)
        self.frame4.columnconfigure([0, 1, 2, 3, 4, 5], weight=1)
        self.frame4.rowconfigure(0, weight=1)
        self.frame5.columnconfigure([0, 1, 2], weight=1)
        self.frame5.rowconfigure(0, weight=1)

    def create_widgets(self):
        self.canvas1 = Canvas(self.frame1, bg='gray40', width=200, height=200, highlightthickness=0)
        self.canvas1.grid(column=0, row=0, sticky='nsew')
        self.canvas2 = Canvas(self.frame2, bg='gray30', width=200, height=200, highlightthickness=0)
        self.canvas2.grid(column=0, row=0, sticky='nsew')
        self.canvas3 = Canvas(self.frame3, bg='gray20', width=200, height=200, highlightthickness=0)
        self.canvas3.grid(column=0, row=0, sticky='nsew')

        self.texto1 = self.canvas1.create_text(1, 1, text='0', font=('Arial', 12, 'bold'), fill='White')
        self.texto2 = self.canvas2.create_text(1, 1, text='0', font=('Arial', 12, 'bold'), fill='White')
        self.texto3 = self.canvas3.create_text(1, 1, text='0', font=('Arial', 12, 'bold'), fill='White')

        self.texto_minutos = self.canvas1.create_text(1, 1, text='Minutos', font=('Arial', 12, 'bold'), fill='White')
        self.texto_segundos = self.canvas2.create_text(1, 1, text='Segundos', font=('Arial', 12, 'bold'), fill='White')
        self.texto_milisegundos = self.canvas3.create_text(1, 1, text='Milisegundos', font=('Arial', 10, 'bold'), fill='White')

        self.circulo1 = self.canvas1.create_rectangle(10, 10, 100, 100, outline='red2', width=10)
        self.circulo2 = self.canvas2.create_rectangle(10, 10, 100, 100, outline='medium spring green', width=10)
        self.circulo3 = self.canvas3.create_rectangle(10, 10, 100, 100, outline='magenta2', width=10)

        self.lectura1 = Label(self.frame4, text='Lectura 1', fg='white', bg='gray10')
        self.lectura1.grid(column=0, row=0, sticky='nsew')
        self.lectura2 = Label(self.frame4, text='Lectura 2', fg='white', bg='gray10')
        self.lectura2.grid(column=1, row=0, sticky='nsew')
        self.lectura3 = Label(self.frame4, text='Lectura 3', fg='white', bg='gray10')
        self.lectura3.grid(column=2, row=0, sticky='nsew')
        self.lectura4 = Label(self.frame4, text='Lectura 4', fg='white', bg='gray10')
        self.lectura4.grid(column=3, row=0, sticky='nsew')
        self.lectura5 = Label(self.frame4, text='Lectura 5', fg='white', bg='gray10')
        self.lectura5.grid(column=4, row=0, sticky='nsew')
        self.lectura6 = Label(self.frame4, text='Lectura 6', fg='white', bg='gray10')
        self.lectura6.grid(column=5, row=0, sticky='nsew')

        self.stop = Button(self.frame5, text='DETENER', relief="raised", bd=5, bg='orange', font=('Arial', 12, 'bold'), width=20, command=self.stop_boton)
        self.stop.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
        self.inicio = Button(self.frame5, text='INICIAR', relief="raised", bd=5, bg='green2', font=('Arial', 12, 'bold'), width=20, command=self.iniciar_pausar)
        self.inicio.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
        self.vuelta = Button(self.frame5, text='VUELTA', relief="raised", bd=4, bg='blue2', font=('Arial', 12, 'bold'), width=20, command=self.vueltas)
        self.vuelta.grid(column=1, row=0, padx=10, pady=10, sticky='nsew')
        self.fin = Button(self.frame5, text='RESTABLECER', relief="raised", bd=4, bg='red2', font=('Arial', 12, 'bold'), width=20, command=self.reiniciar)
        self.fin.grid(column=2, row=0, padx=10, pady=10, sticky='nsew')

    def iniciar_pausar(self):
        self.ml += 1
        if self.ml == 999:
            self.ml = 0
            self.se += 1
            if self.se == 59:
                self.se = 0
                self.mi += 1
        self.contar = self.inicio.after(1, self.iniciar_pausar)
        self.clik_inicio = self.inicio.grid_forget()
        if self.clik_inicio is None:
            self.stop.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
            self.stop.config(bg='orange', text='DETENER')
        
        #Registrar datos probando
        

    def stop_boton(self):
        self.clik_stop = self.stop.grid_forget()
        if self.clik_stop is None:
            self.inicio.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
            self.inicio.config(bg='aqua', text='CONTINUAR')
            self.inicio.after_cancel(self.contar)

    def vueltas(self):
        self.click_lectura += 1
        lectura = '{} → {}:{}:{}'.format(self.click_lectura, self.mi, self.se, self.ml)
        if self.click_lectura == 1:
            self.lectura1.config(text=lectura, fg='white', bg='gray10')
        elif self.click_lectura == 2:
            self.lectura2.config(text=lectura, fg='white', bg='gray10')
        elif self.click_lectura == 3:
            self.lectura3.config(text=lectura, fg='white', bg='gray10')
        elif self.click_lectura == 4:
            self.lectura4.config(text=lectura, fg='white', bg='gray10')
        elif self.click_lectura == 5:
            self.lectura5.config(text=lectura, fg='white', bg='gray10')
        elif self.click_lectura == 6:
            self.lectura6.config(text=lectura, fg='white', bg='gray10')
            self.click_lectura = 0

    def reiniciar(self):
        self.mi = 0
        self.se = 0
        self.ml = 0
        self.click_lectura = 0
        self.inicio.after_cancel(self.contar)
        self.lectura1.configure(text='Lectura 1', fg='white', bg='gray10')
        self.lectura2.configure(text='Lectura 2', fg='white', bg='gray10')
        self.lectura3.configure(text='Lectura 3', fg='white', bg='gray10')
        self.lectura4.configure(text='Lectura 4', fg='white', bg='gray10')
        self.lectura5.configure(text='Lectura 5', fg='white', bg='gray10')
        self.lectura6.configure(text='Lectura 6', fg='white', bg='gray10')
        self.stop.grid_forget()
        self.inicio.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
        self.inicio.config(bg='green2', text='INICIAR')

    def coordenadas(self):
        x = self.canvas1.winfo_width()
        y = self.canvas1.winfo_height()
        x1 = int(x - 0.1 * x - 0.1 * y + 25)
        y1 = int(y - 0.1 * x - 0.1 * y + 20)
        x2 = int(x - 0.4 * x - 0.4 * y - 15)
        y2 = int(y - 0.4 * x - 0.4 * y - 30)
        tamano = int(y1 * 0.2 + x1 * 0.1 + 10)
        tamano_texto = int(y1 * 0.02 + x1 * 0.02 + 3)
        self.canvas1.coords(self.circulo1, x1, y1, x2, y2)
        self.canvas2.coords(self.circulo2, x1, y1, x2, y2)
        self.canvas3.coords(self.circulo3, x1, y1, x2, y2)

        z1 = int(x1 * 0.6 - 10)
        z2 = int(y1 * 0.6 - 10)
        w1 = int(x1 * 0.49 + 8)
        w2 = int(y1 * 0.8 + 10)
        self.canvas1.coords(self.texto1, z1, z2)
        self.canvas2.coords(self.texto2, z1, z2)
        self.canvas3.coords(self.texto3, z1, z2)
        self.canvas1.itemconfig(self.texto1, font=('Arial', tamano, 'bold'), text=self.mi)
        self.canvas2.itemconfig(self.texto2, font=('Arial', tamano, 'bold'), text=self.se)
        self.canvas3.itemconfig(self.texto2, font=('Arial', tamano, 'bold'), text=self.ml)
        self.canvas1.coords(self.texto_minutos, w1, w2)
        self.canvas2.coords(self.texto_segundos, w1, w2)
        self.canvas3.coords(self.texto_milisegundos, w1, w2)
        self.canvas1.itemconfig(self.texto_minutos, font=('Arial', tamano_texto, 'bold'))
        self.canvas2.itemconfig(self.texto_segundos, font=('Arial', tamano_texto, 'bold'))
        self.canvas3.itemconfig(self.texto_milisegundos, font=('Arial', tamano_texto, 'bold'))

        self.canvas1.after(1000, self.coordenadas)

    def run(self):
        self.ventana.mainloop()