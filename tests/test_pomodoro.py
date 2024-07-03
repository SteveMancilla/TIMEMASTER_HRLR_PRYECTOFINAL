import unittest
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication
from Pomodoro import Pomodoro

class TestPomodoroBasic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Necesario para PyQt5

    def setUp(self):
        # Inicializar la instancia de Pomodoro
        self.pomodoro = Pomodoro()

        # Mockeamos la base de datos y los elementos necesarios
        self.pomodoro.db = MagicMock()
        self.pomodoro.session = MagicMock()
        self.pomodoro.usuario = MagicMock()
        self.pomodoro.usuario.Usuario_ID = 1

        # Establecer valores iniciales para los campos desplegables
        self.pomodoro.cbMinutosTrabajoPom.setCurrentText("1")
        self.pomodoro.cbMinDescansoPom.setCurrentText("1")

    def test_iniciar_timer_trabajo(self):
        """Verifica que al iniciar el temporizador de trabajo, el tiempo restante se establece correctamente."""
        self.pomodoro.start_timer()
        self.assertEqual(self.pomodoro.time_remaining, 60)  # 1 minuto = 60 segundos

    def test_actualizar_timer_trabajo(self):
        """Verifica que el temporizador de trabajo actualiza el tiempo restante."""
        self.pomodoro.time_remaining = 10  # 10 segundos
        self.pomodoro.update_timer_trabajo()
        self.assertEqual(self.pomodoro.time_remaining, 9)  # Debería decrementar a 9 segundos

    def test_iniciar_timer_descanso(self):
        """Verifica que al iniciar el temporizador de descanso, el tiempo restante se establece correctamente."""
        self.pomodoro.cbMinDescansoPom.setCurrentText("2")  # 2 minutos
        self.pomodoro.startDescanso()
        self.assertEqual(self.pomodoro.time_remaining, 120)  # 2 minutos = 120 segundos

    def test_actualizar_timer_descanso(self):
        """Verifica que el temporizador de descanso actualiza el tiempo restante."""
        self.pomodoro.time_remaining = 5  # 5 segundos
        self.pomodoro.update_timer_descanso()
        self.assertEqual(self.pomodoro.time_remaining, 4)  # Debería decrementar a 4 segundos

    def test_iniciar_y_detener_timer(self):
        """Verifica que iniciar y detener el temporizador funciona como se espera."""
        self.pomodoro.start_timer()
        self.assertTrue(self.pomodoro.timer.isActive())  # El temporizador debe estar activo
        self.pomodoro.detener()
        self.assertFalse(self.pomodoro.timer.isActive())  # El temporizador debe estar detenido
    
    def test_reanudar_timer(self):
        """Verifica que reanudar el temporizador reinicia el temporizador."""
        self.pomodoro.start_timer()
        self.pomodoro.detener()
        self.pomodoro.reanudar()
        self.assertTrue(self.pomodoro.timer.isActive())  # El temporizador debe estar activo después de reanudar

if __name__ == '__main__':
    unittest.main()
