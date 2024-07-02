#NO BORRAR

from tkinter import messagebox, Label, Entry, ttk, Toplevel, Button
from time import strftime
from pygame import mixer
import threading
import time
from src.modelo.db import DB, PomodoroModel, AuditoriaModel, UsuarioModel

class Pomodoro:
    def __init__(self, master):
        self.master = master
        self.ventana = Toplevel(self.master)
        self.ventana.config(bg='black')
        self.ventana.geometry('600x300')
        self.ventana.title('Pomodoro')
        self.ventana.minsize(width=500, height=300)
        mixer.init()

        self.db = DB()
        self.session = self.db.get_session()

        # Obtener el último usuario registrado
        self.usuario = self.session.query(UsuarioModel).order_by(UsuarioModel.Usuario_ID.desc()).first()
        if self.usuario is None:
            messagebox.showerror("Error", "No se encontró ningún usuario registrado")
            self.ventana.destroy()
            return

        self.tiempo_trabajo = 0
        self.tiempo_descanso = 0
        self.timer_active = False

        self.create_widgets()

        self.texto_hora = Label(self.ventana, fg='aqua', bg='black', font=('Arial', 30, 'bold'))
        self.texto_hora.grid(row=1, column=0, columnspan=3, sticky="nsew", ipadx=5, ipady=20)
        self.obtener_tiempo()

        self.timer_label = Label(self.ventana, fg='yellow', bg='black', font=('Arial', 24, 'bold'))
        self.timer_label.grid(row=2, column=0, columnspan=3, sticky="nsew", ipadx=5, ipady=10)

    def create_widgets(self):
        text1 = Label(self.ventana, text='Tiempo de trabajo (minutos)', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        text1.grid(row=3, column=0, padx=5, pady=5)

        self.trabajoPomodoro = Entry(self.ventana, bg='white', fg='green', font=('Arial',12,'bold'))
        self.trabajoPomodoro.grid(row=3, column=1, padx=5, pady=5)

        text2 = Label(self.ventana, text='Tiempo de descanso (minutos)', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        text2.grid(row=4, column=0, padx=5, pady=5)

        self.descansoPomodoro = Entry(self.ventana, bg='white', fg='green', font=('Arial',12,'bold'))
        self.descansoPomodoro.grid(row=4, column=1, padx=5, pady=5)

        btnestablcerconfiguracionPomodoro = Button(self.ventana, text='Configuracion', bg='blue', fg='white', font=('Arial', 12, 'bold'), command=self.establecer_configuracion)
        btnestablcerconfiguracionPomodoro.grid(row=20, column=0, padx=5, pady=5)

        self.btniniciarTrabajoPomodoro = Button(self.ventana, text='Iniciar Trabajo', bg='blue', fg='white', font=('Arial', 12, 'bold'), command=self.iniciar_trabajo)
        self.btniniciarTrabajoPomodoro.grid(row=20, column=1, padx=5, pady=5)

        self.btniniciarDescansoPomodoro = Button(self.ventana, text='Iniciar Descanso', bg='blue', fg='white', font=('Arial', 12, 'bold'), command=self.iniciar_descanso)
        self.btniniciarDescansoPomodoro.grid(row=20, column=2, padx=5, pady=5)
        self.btniniciarDescansoPomodoro.config(state='disabled')

    def obtener_tiempo(self):
        hora = strftime('%H:%M:%S')
        self.texto_hora.config(text=hora)
        self.texto_hora.after(1000, self.obtener_tiempo)

    def establecer_configuracion(self):
        try:
            self.tiempo_trabajo = float(self.trabajoPomodoro.get())
            self.tiempo_descanso = float(self.descansoPomodoro.get())

            pomodoro = PomodoroModel(
                temPom_Duracion_trabajo=self.tiempo_trabajo,
                temPom_Duracion_descanso=self.tiempo_descanso,
                Usuario_ID=self.usuario.Usuario_ID
            )
            self.session.add(pomodoro)
            self.session.commit()

            self.db.register_audit(self.session, self.usuario.Usuario_ID, "Configuración de Pomodoro")

            messagebox.showinfo("Configuración", "Configuración guardada exitosamente")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la configuración: {str(e)}")

    def iniciar_trabajo(self):
        if self.tiempo_trabajo > 0:
            self.btniniciarTrabajoPomodoro.config(state='disabled')
            self.btniniciarDescansoPomodoro.config(state='disabled')
            self.timer_active = True
            threading.Thread(target=self.countdown, args=(int(self.tiempo_trabajo * 60), "Trabajo")).start()
        else:
            messagebox.showerror("Error", "Por favor, configure el tiempo de trabajo primero")

    def iniciar_descanso(self):
        if self.tiempo_descanso > 0:
            self.btniniciarTrabajoPomodoro.config(state='disabled')
            self.btniniciarDescansoPomodoro.config(state='disabled')
            self.timer_active = True
            threading.Thread(target=self.countdown, args=(int(self.tiempo_descanso * 60), "Descanso")).start()
        else:
            messagebox.showerror("Error", "Por favor, configure el tiempo de descanso primero")

    def countdown(self, t, mode):
        while t >= 0 and self.timer_active:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            self.ventana.after(0, self.update_timer_label, timeformat, mode)
            time.sleep(1)
            t -= 1

        if self.timer_active:
            self.ventana.after(0, self.play_alarm)
            self.ventana.after(0, self.show_finish_message, mode)
        
        self.timer_active = False
        self.ventana.after(0, self.reset_buttons)

    def update_timer_label(self, timeformat, mode):
        self.timer_label.config(text=f"{mode}: {timeformat}")

    def clear_timer_label(self):
        self.timer_label.config(text="")

    def play_alarm(self):
        mixer.music.load("sound.mp3")  # Reemplaza con la ruta de tu archivo de sonido
        mixer.music.play()

    def show_finish_message(self, mode):
        if mode == "Trabajo":
            messagebox.showinfo("Pomodoro", "¡Tiempo de trabajo finalizado!")
        else:
            messagebox.showinfo("Pomodoro", "¡Tiempo de descanso finalizado!")

    def reset_buttons(self):
        self.btniniciarTrabajoPomodoro.config(state='normal')
        self.btniniciarDescansoPomodoro.config(state='normal')
        self.clear_timer_label()
    
    def run(self):
        self.ventana.mainloop()

    def __del__(self):
        self.session.close()
        self.db.close()