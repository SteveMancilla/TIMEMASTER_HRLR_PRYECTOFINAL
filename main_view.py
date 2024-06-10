import tkinter as tk
import sys
'''sys.path.insert(0, 'src')
sys.path.insert(0, 'D:\A_ProyectoConstruccionSoftware\TIMEMASTER_HRLR_PRYECTOFINAL\src\modelo\db.py')'''

from tkinter import messagebox
from src.modelo.timer import Timer
from src.modelo.alarm import Alarm
from src.modelo.pomodoro import Pomodoro

class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Timemaster")

        self.timer_frame = tk.Frame(self.root)
        self.timer_frame.pack()

        self.alarm_frame = tk.Frame(self.root)
        self.alarm_frame.pack()

        self.pomodoro_frame = tk.Frame(self.root)
        self.pomodoro_frame.pack()

        self.timer_label = tk.Label(self.timer_frame, text="Temporizador")
        self.timer_label.pack()

        self.timer_entry = tk.Entry(self.timer_frame)
        self.timer_entry.pack()

        self.timer_start_button = tk.Button(self.timer_frame, text="Iniciar", command=self.start_timer)
        self.timer_start_button.pack()

        self.timer_pause_button = tk.Button(self.timer_frame, text="Pausar", command=self.pause_timer)
        self.timer_pause_button.pack()

        self.timer_reset_button = tk.Button(self.timer_frame, text="Reiniciar", command=self.reset_timer)
        self.timer_reset_button.pack()

        self.timer_stop_button = tk.Button(self.timer_frame, text="Detener", command=self.stop_timer)
        self.timer_stop_button.pack()

        self.alarm_label = tk.Label(self.alarm_frame, text="Alarma")
        self.alarm_label.pack()

        self.alarm_time_entry = tk.Entry(self.alarm_frame)
        self.alarm_time_entry.pack()

        self.alarm_set_button = tk.Button(self.alarm_frame, text="Configurar", command=self.set_alarm)
        self.alarm_set_button.pack()

        self.alarm_check_button = tk.Button(self.alarm_frame, text="Verificar", command=self.check_alarm)
        self.alarm_check_button.pack()

        self.pomodoro_label = tk.Label(self.pomodoro_frame, text="Temporizador Pomodoro")
        self.pomodoro_label.pack()

        self.pomodoro_work_entry = tk.Entry(self.pomodoro_frame)
        self.pomodoro_work_entry.pack()

        self.pomodoro_break_entry = tk.Entry(self.pomodoro_frame)
        self.pomodoro_break_entry.pack()

        self.pomodoro_start_button = tk.Button(self.pomodoro_frame, text="Iniciar", command=self.start_pomodoro)
        self.pomodoro_start_button.pack()

        self.pomodoro_pause_button = tk.Button(self.pomodoro_frame, text="Pausar", command=self.pause_pomodoro)
        self.pomodoro_pause_button.pack()

        self.pomodoro_reset_button = tk.Button(self.pomodoro_frame, text="Reiniciar", command=self.reset_pomodoro)
        self.pomodoro_reset_button.pack()

        self.pomodoro_stop_button = tk.Button(self.pomodoro_frame, text="Detener", command=self.stop_pomodoro)
        self.pomodoro_stop_button.pack()

    def start_timer(self):
        duration = float(self.timer_entry.get())
        self.timer = Timer(duration)
        self.timer.start()
        self.update_timer()

    def pause_timer(self):
        self.timer.stop()

    def reset_timer(self):
        self.timer.reset()

    def stop_timer(self):
        self.timer.stop()
        self.timer_label.config(text="Temporizador detenido")

    def set_alarm(self):
        alarm_time = float(self.alarm_time_entry.get())
        self.alarm = Alarm(alarm_time)
        self.alarm.set()
        self.alarm_label.config(text="Alarma configurada")

    def check_alarm(self):
        if self.alarm.check():
            messagebox.showinfo("Alarma", "¡La alarma ha sonado!")
        else:
            messagebox.showinfo("Alarma", "Aún no es hora de la alarma")

    def start_pomodoro(self):
        work_time = float(self.pomodoro_work_entry.get())
        break_time = float(self.pomodoro_break_entry.get())
        self.pomodoro = Pomodoro(work_time, break_time)
        self.pomodoro.start()
        self.update_pomodoro()

    def pause_pomodoro(self):
        self.pomodoro.stop()

    def reset_pomodoro(self):
        self.pomodoro.reset()

    def stop_pomodoro(self):
        self.pomodoro.stop()
        self.pomodoro_label.config(text="Pomodoro detenido")

    def update_timer(self):
        if self.timer.is_running:
            remaining_time = self.timer.get_remaining_time()
            self.timer_label.config(text=f"Tiempo restante: {remaining_time:.2f} segundos")
            self.timer_label.after(100, self.update_timer)
        else:
            self.timer_label.config(text="Temporizador detenido")
            messagebox.showinfo("Temporizador", "¡El temporizador ha finalizado!")

    def update_pomodoro(self):
        if self.pomodoro.is_running:
            remaining_time = self.pomodoro.get_remaining_time()
            if remaining_time < self.pomodoro.work_time:
                self.pomodoro_label.config(text=f"Tiempo de trabajo restante: {remaining_time:.2f} segundos")
            else:
                self.pomodoro_label.config(text=f"Tiempo de descanso restante: {remaining_time:.2f} segundos")
            self.pomodoro_label.after(100, self.update_pomodoro)
        else:
            self.pomodoro_label.config(text="Pomodoro detenido")
            messagebox.showinfo("Pomodoro", "¡El temporizador Pomodoro ha finalizado!")

if __name__ == '__main__':
    view = MainView()
    view.root.mainloop()