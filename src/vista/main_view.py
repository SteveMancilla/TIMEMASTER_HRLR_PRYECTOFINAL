import threading
from datetime import datetime, time
import tkinter as tk
from tkinter import messagebox, ttk
from src.modelo.timer import Timer
from src.modelo.alarm import Alarm
from src.modelo.pomodoro import Pomodoro
from src.modelo.db import DB, TimerModel, AlarmModel, PomodoroModel, UsuarioModel
from playsound import playsound
from pygame import mixer

class MainView:
    def __init__(self, user_data):
        self.root = tk.Tk()
        self.root.title("Timemaster")
        
        # Crear la base de datos
        self.db = DB()
        self.session = self.db.get_session()

        # Solicitar datos del usuario
        self.user_id = self.register_user(user_data)

        self.create_widgets()
        self.create_clock()
        self.sound_thread = None

        mixer.init()

    def register_user(self, user_data):
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

        self.alarm_time_frame = tk.Frame(self.alarm_frame, bg='lightgreen')
        self.alarm_time_frame.pack(pady=5)

        self.alarm_hour = ttk.Combobox(self.alarm_time_frame, values=list(range(24)), width=5, justify='center')
        self.alarm_hour.pack(side=tk.LEFT, padx=5)
        self.alarm_hour.current(0)

        self.alarm_minute = ttk.Combobox(self.alarm_time_frame, values=list(range(60)), width=5, justify='center')
        self.alarm_minute.pack(side=tk.LEFT, padx=5)
        self.alarm_minute.current(0)

        self.alarm_second = ttk.Combobox(self.alarm_time_frame, values=list(range(60)), width=5, justify='center')
        self.alarm_second.pack(side=tk.LEFT, padx=5)
        self.alarm_second.current(0)

        self.alarm_label = tk.Label(self.alarm_frame, text="Alarma configurada: ", bg='lightgreen')
        self.alarm_label.pack()

        tk.Button(self.alarm_frame, text="Configurar", command=self.set_alarm).pack()

    def create_pomodoro_widgets(self):
        tk.Label(self.pomodoro_frame, text="Pomodoro", bg='lightcoral').pack()

        self.pomodoro_work_entry = tk.Entry(self.pomodoro_frame)
        self.pomodoro_work_entry.pack()

        self.pomodoro_break_entry = tk.Entry(self.pomodoro_frame)
        self.pomodoro_break_entry.pack()

        self.pomodoro_label = tk.Label(self.pomodoro_frame, text="Tiempo de trabajo restante: ", bg='lightcoral')
        self.pomodoro_label.pack()

        tk.Button(self.pomodoro_frame, text="Iniciar", command=self.start_pomodoro).pack()
        tk.Button(self.pomodoro_frame, text="Pausar", command=self.pause_pomodoro).pack()
        tk.Button(self.pomodoro_frame, text="Reiniciar", command=self.reset_pomodoro).pack()

    def start_timer(self):
        try:
            duration = float(self.timer_entry.get())
            self.timer = Timer(duration)
            self.timer.start()
            self.update_timer()

            # Registrar auditoría y guardar temporizador en la base de datos
            audit = self.db.register_audit(self.session, self.user_id, 'Iniciar temporizador')
            timer_model = TimerModel(
                temporizador_Tiempo=duration, 
                temporizador_estado='Iniciado', 
                Usuario_ID=self.user_id,
                Auditoria_ID=audit.Auditoria_ID
            )
            self.session.add(timer_model)
            self.session.commit()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico para la duración del temporizador.")

    def pause_timer(self):
        if self.timer.is_running:
            self.timer.stop()
        else:
            self.timer.start()
            self.update_timer()

    def reset_timer(self):
        self.timer.reset()
        self.update_timer()

    def set_alarm(self):
        try:
            alarm_hour = int(self.alarm_hour.get())
            alarm_minute = int(self.alarm_minute.get())
            alarm_second = int(self.alarm_second.get())

            # Validar que los valores están en los rangos correctos
            if not (0 <= alarm_hour < 24) or not (0 <= alarm_minute < 60) or not (0 <= alarm_second < 60):
                raise ValueError

            # Formatear la hora utilizando strftime
            alarm_time = time(alarm_hour, alarm_minute, alarm_second).strftime('%H:%M:%S')
            self.alarm = Alarm(alarm_time)
            self.alarm.set()
            self.alarm_label.config(text="Alarma configurada para las " + alarm_time)

            # Registrar auditoría y guardar alarma en la base de datos
            audit = self.db.register_audit(self.session, self.user_id, 'Configurar alarma')
            alarm_model = AlarmModel(
                Alarma_Hora_Programada=self.alarm.alarm_time, 
                Alarma_Estado='Programada',
                Usuario_ID=self.user_id,
                Auditoria_ID=audit.Auditoria_ID
            )
            self.session.add(alarm_model)
            self.session.commit()
        except ValueError:
            messagebox.showerror("Error", "Formato de tiempo inválido. Use HH:MM:SS.")

    def check_alarm(self):
        if self.alarm and self.alarm.check():
            messagebox.showinfo("Alarma", "¡La alarma ha sonado!")
            self.start_sound()
        else:
            messagebox.showinfo("Alarma", "Aún no es hora de la alarma o no hay una alarma configurada.")

    def start_pomodoro(self):
        try:
            work_time = float(self.pomodoro_work_entry.get())
            break_time = float(self.pomodoro_break_entry.get())
            self.pomodoro = Pomodoro(work_time, break_time)
            self.pomodoro.start()
            self.update_pomodoro()

            # Registrar auditoría y guardar pomodoro en la base de datos
            audit = self.db.register_audit(self.session, self.user_id, 'Iniciar pomodoro')
            pomodoro_model = PomodoroModel(
                temPom_Duracion_trabajo=work_time, 
                temPom_Duracion_descanso=break_time, 
                Usuario_ID=self.user_id,
                Auditoria_ID=audit.Auditoria_ID
            )
            self.session.add(pomodoro_model)
            self.session.commit()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos para los tiempos de trabajo y descanso.")

    def pause_pomodoro(self):
        if self.pomodoro.is_running:
            self.pomodoro.stop()
        else:
            self.pomodoro.start()
            self.update_pomodoro()

    def reset_pomodoro(self):
        self.pomodoro.reset()
        self.update_pomodoro()

    def update_timer(self):
        if self.timer.is_running:
            remaining_time = self.timer.get_remaining_time()
            self.timer_label.config(text=f"Tiempo restante: {remaining_time:.2f} segundos")
            self.root.after(100, self.update_timer)
        else:
            if self.timer.is_finished():
                messagebox.showinfo("Temporizador", "¡El temporizador ha finalizado!")
                self.start_sound()
            self.timer_label.config(text="Temporizador detenido")

    def update_pomodoro(self):
        if self.pomodoro.is_running:
            remaining_time = self.pomodoro.get_remaining_time()
            self.pomodoro_label.config(text=f"Tiempo de descanso restante: {remaining_time:.2f} segundos")
            self.root.after(100, self.update_pomodoro)
        else:
            if self.pomodoro.is_finished():
                if self.pomodoro.is_break:
                    messagebox.showinfo("Pomodoro", "¡Es hora de descansar!")
                else:
                    messagebox.showinfo("Pomodoro", "¡Es hora de trabajar!")
                self.start_sound()
            else:
                self.pomodoro_label.config(text="Pomodoro detenido")

    def start_sound(self):
        if self.sound_thread and self.sound_thread.is_alive():
            return
        self.sound_thread = threading.Thread(target=self.play_sound)
        self.sound_thread.start()
        self.create_stop_sound_button()

    def play_sound(self):
        playsound("sound.mp3")

    def stop_sound(self):
        if self.sound_thread and self.sound_thread.is_alive():
            self.sound_thread = None
        if hasattr(self, 'stop_sound_button'):
            self.stop_sound_button.destroy()

    def create_stop_sound_button(self):
        self.stop_sound_button = tk.Button(self.root, text="Detener sonido", command=self.stop_sound)
        self.stop_sound_button.pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    user_data = {
        "nombre": "Usuario",
        "apellido": "Ejemplo",
        "celular": "1234567890",
        "email": "usuario@ejemplo.com"
    }
    app = MainView(user_data)
    app.run()
