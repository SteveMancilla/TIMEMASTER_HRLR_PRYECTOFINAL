from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from src.modelo.timer import Timer
from src.modelo.alarm import Alarm
from src.modelo.pomodoro import Pomodoro
from src.modelo.db import DB, TimerModel, AlarmModel, PomodoroModel, UsuarioModel
from playsound import playsound
from threading import Thread

class MainView:
    def __init__(self, user_data):
        self.root = tk.Tk()
        self.root.title("Timemaster")
        
        # Crear la base de datos
        self.db = DB()
        self.session = self.db.get_session()

        # Datos del usuario
        self.user_id = self.get_user_data(user_data)

        self.create_widgets()
        self.create_clock()

    def get_user_data(self, user_data):
        usuario = UsuarioModel(
            Usuario_Nombre=user_data["nombre"],
            Usuario_Apellido_Paterno=user_data["apellido"],
            Usuario_Celular=user_data["celular"],
            Usuario_Email=user_data["email"]
        )
        self.session.add(usuario)
        self.session.commit()

        return usuario.Usuario_ID

    def create_widgets(self):
        self.timer_frame = tk.Frame(self.root, bg='lightblue')
        self.timer_frame.pack(pady=10)

        self.alarm_frame = tk.Frame(self.root, bg='lightgreen')
        self.alarm_frame.pack(pady=10)

        self.pomodoro_frame = tk.Frame(self.root, bg='lightcoral')
        self.pomodoro_frame.pack(pady=10)

        self.create_timer_widgets()
        self.create_alarm_widgets()
        self.create_pomodoro_widgets()

    def create_clock(self):
        self.clock_label = tk.Label(self.root, font=('Helvetica', 14))
        self.clock_label.pack(side=tk.TOP)
        self.update_clock()

    def update_clock(self):
        now = datetime.now().strftime('%H:%M:%S')
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)

    def create_timer_widgets(self):
        tk.Label(self.timer_frame, text="Temporizador", bg='lightblue').pack()

        self.timer_entry = tk.Entry(self.timer_frame)
        self.timer_entry.pack()

        self.timer_label = tk.Label(self.timer_frame, text="Tiempo restante: ", bg='lightblue')
        self.timer_label.pack()

        tk.Button(self.timer_frame, text="Iniciar", command=self.start_timer).pack()
        tk.Button(self.timer_frame, text="Pausar", command=self.pause_timer).pack()
        tk.Button(self.timer_frame, text="Reiniciar", command=self.reset_timer).pack()

    def create_alarm_widgets(self):
        tk.Label(self.alarm_frame, text="Alarma", bg='lightgreen').pack()

        self.alarm_time_entry = tk.Entry(self.alarm_frame)
        self.alarm_time_entry.pack()

        self.alarm_label = tk.Label(self.alarm_frame, text="Alarma configurada: ", bg='lightgreen')
        self.alarm_label.pack()

        tk.Button(self.alarm_frame, text="Configurar", command=self.set_alarm).pack()

    def create_pomodoro_widgets(self):
        tk.Label(self.pomodoro_frame, text="Pomodoro", bg='lightcoral').pack()

        tk.Label(self.pomodoro_frame, text="Duración de trabajo (min)", bg='lightcoral').pack()
        self.work_time_entry = tk.Entry(self.pomodoro_frame)
        self.work_time_entry.pack()

        tk.Label(self.pomodoro_frame, text="Duración de descanso (min)", bg='lightcoral').pack()
        self.break_time_entry = tk.Entry(self.pomodoro_frame)
        self.break_time_entry.pack()

        self.pomodoro_label = tk.Label(self.pomodoro_frame, text="Estado: ", bg='lightcoral')
        self.pomodoro_label.pack()

        tk.Button(self.pomodoro_frame, text="Iniciar", command=self.start_pomodoro).pack()
        tk.Button(self.pomodoro_frame, text="Pausar", command=self.pause_pomodoro).pack()
        tk.Button(self.pomodoro_frame, text="Reiniciar", command=self.reset_pomodoro).pack()

    def start_timer(self):
        duration = float(self.timer_entry.get())
        self.timer = Timer(duration)
        self.timer.start()
        self.db.register_audit(self.session, self.user_id, "Temporizador Iniciado")
        self.update_timer()

    def pause_timer(self):
        if self.timer:
            self.timer.stop()
            self.db.register_audit(self.session, self.user_id, "Temporizador Pausado")

    def reset_timer(self):
        if self.timer:
            self.timer.reset()
            self.db.register_audit(self.session, self.user_id, "Temporizador Reiniciado")
        self.update_timer()

    def update_timer(self):
        if self.timer:
            remaining_time = self.timer.get_remaining_time()
            self.timer_label.config(text=f"Tiempo restante: {remaining_time:.2f} segundos")
            if self.timer.is_finished():
                self.play_sound()
                self.db.register_audit(self.session, self.user_id, "Temporizador Finalizado")
                return
            self.root.after(1000, self.update_timer)

    def set_alarm(self):
        alarm_time = self.alarm_time_entry.get()
        self.alarm = Alarm(alarm_time)
        self.alarm.set()
        self.db.register_audit(self.session, self.user_id, "Alarma Configurada")
        self.update_alarm()

    def update_alarm(self):
        if self.alarm and self.alarm.check():
            self.play_sound()
            self.db.register_audit(self.session, self.user_id, "Alarma Sonando")
            return
        self.root.after(1000, self.update_alarm)

    def start_pomodoro(self):
        work_time = float(self.work_time_entry.get())
        break_time = float(self.break_time_entry.get())
        self.pomodoro = Pomodoro(work_time, break_time)
        self.pomodoro.start()
        self.db.register_audit(self.session, self.user_id, "Pomodoro Iniciado")
        self.update_pomodoro()

    def pause_pomodoro(self):
        if self.pomodoro:
            self.pomodoro.stop()
            self.db.register_audit(self.session, self.user_id, "Pomodoro Pausado")

    def reset_pomodoro(self):
        if self.pomodoro:
            self.pomodoro.reset()
            self.db.register_audit(self.session, self.user_id, "Pomodoro Reiniciado")
        self.update_pomodoro()

    def update_pomodoro(self):
        if self.pomodoro:
            remaining_time = self.pomodoro.get_remaining_time()
            estado = "Trabajo" if not self.pomodoro.is_break else "Descanso"
            self.pomodoro_label.config(text=f"Estado: {estado}, Tiempo restante: {remaining_time:.2f} segundos")
            if self.pomodoro.is_finished():
                self.pomodoro.switch()
                self.db.register_audit(self.session, self.user_id, f"Pomodoro {'Trabajo' if self.pomodoro.is_break else 'Descanso'} Finalizado")
                self.play_sound()
            self.root.after(1000, self.update_pomodoro)

    def play_sound(self):
        def play():
            playsound("sound.mp3")
        Thread(target=play).start()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    user_data = {
        "nombre": simpledialog.askstring("Nombre", "Ingrese su nombre"),
        "apellido": simpledialog.askstring("Apellido", "Ingrese su apellido paterno"),
        "celular": simpledialog.askstring("Celular", "Ingrese su celular"),
        "email": simpledialog.askstring("Email", "Ingrese su email")
    }
    main_view = MainView(user_data)
    main_view.run()


