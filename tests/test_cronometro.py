import unittest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication
from Cronometro import Cronometro  # Asegúrate de que el archivo se llame Cronometro.py

class TestCronometro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Necesario para PyQt5

    def setUp(self):
        # Inicializar la instancia de Cronometro
        self.cronometro = Cronometro()

        # Mockeamos la base de datos y los elementos necesarios
        self.cronometro.db = MagicMock()
        self.cronometro.session = MagicMock()
        self.cronometro.usuario = MagicMock()
        self.cronometro.usuario.Usuario_ID = 1

        # Mocks para evitar interacciones con archivos y audio
        self.patcher_load = patch('Cronometro.mixer.music.load')
        self.patcher_play = patch('Cronometro.mixer.music.play')
        self.mock_load = self.patcher_load.start()
        self.mock_play = self.patcher_play.start()

        # Establecer valores iniciales para los campos desplegables
        self.cronometro.cbMinutosTrabajoCrono.setCurrentText("1")
        self.cronometro.cbMinDescansoCrono.setCurrentText("1")

    def tearDown(self):
        self.patcher_load.stop()
        self.patcher_play.stop()

    def test_iniciar_cronometro_min(self):
        """Verifica que al iniciar el cronómetro de minutos, el tiempo restante se establece correctamente."""
        self.cronometro.start_cronometroMin()
        self.assertEqual(self.cronometro.time_remaining, 60)  # 1 minuto = 60 segundos
    
    def test_actualizar_cronometro_min(self):
        """Verifica que el cronómetro de minutos actualiza el tiempo restante."""
        self.cronometro.time_remaining = 10  # 10 segundos
        self.cronometro.update_CronometroMin()
        self.assertEqual(self.cronometro.time_remaining, 9)  # Debería decrementar a 9 segundos
    
    def test_iniciar_cronometro_seg(self):
        """Verifica que al iniciar el cronómetro de segundos, el tiempo restante se establece correctamente."""
        self.cronometro.cbMinDescansoCrono.setCurrentText("2")  # 2 segundos
        self.cronometro.start_cronometroSeg()
        self.assertEqual(self.cronometro.time_remaining, 2)  # 2 segundos
    
    def test_actualizar_cronometro_seg(self):
        """Verifica que el cronómetro de segundos actualiza el tiempo restante."""
        self.cronometro.time_remaining = 5  # 5 segundos
        self.cronometro.update_CronometroSeg()
        self.assertEqual(self.cronometro.time_remaining, 4)  # Debería decrementar a 4 segundos
    
    def test_guardar_minutos(self):
        """Verifica que guardarminutos crea una instancia de TimerModel con los datos correctos y llama al método de adición a la base de datos."""
        self.cronometro.cbMinutosTrabajoCrono.setCurrentText("25")
        self.cronometro.cbMinDescansoCrono.setCurrentText("5")
        self.cronometro.guardarminutos()
        self.cronometro.db.register_audit.assert_called_once_with(self.cronometro.session, 1, "Configuracion de Cronometro")
        self.cronometro.session.add.assert_called_once()
        self.cronometro.session.commit.assert_called_once()
    
    def test_guardar_segundos(self):
        """Verifica que guardarseg crea una instancia de TimerModel con los datos correctos y llama al método de adición a la base de datos."""
        self.cronometro.cbMinutosTrabajoCrono.setCurrentText("10")
        self.cronometro.cbMinDescansoCrono.setCurrentText("20")
        self.cronometro.guardarseg()
        self.cronometro.db.register_audit.assert_called_once_with(self.cronometro.session, 1, "Configuracion de pomodoro")
        self.cronometro.session.add.assert_called_once()
        self.cronometro.session.commit.assert_called_once()

    def test_detener_timer(self):
        """Verifica que detener el cronómetro funciona como se espera."""
        self.cronometro.start_cronometroMin()
        self.cronometro.detener()
        self.assertFalse(self.cronometro.tim.isActive())  # El temporizador de minutos debe estar detenido
        self.assertTrue(self.cronometro.is_paused_min)  # La bandera de pausa debe estar activada
    
    def test_reanudar_timer(self):
        """Verifica que reanudar el cronómetro reinicia el temporizador de minutos."""
        self.cronometro.start_cronometroMin()
        self.cronometro.detener()
        self.cronometro.reanudar()
        self.assertTrue(self.cronometro.tim.isActive())  # El temporizador de minutos debe estar activo después de reanudar
    
    def test_mostrar_hora_actual(self):
        """Verifica que se muestra la hora actual en el LCD."""
        with patch('Cronometro.QTime.currentTime') as mock_time:
            mock_time.return_value.toString.return_value = '12:34:56'
            self.cronometro.mostrarHoraActual()
            self.assertEqual(self.cronometro.lcdNumberHoraActual.text(), '12:34:56')
    
    def test_toggle_maximize_restore(self):
        """Verifica que la ventana cambia entre maximizado y restaurado."""
        self.cronometro.showMaximized = MagicMock()
        self.cronometro.showNormal = MagicMock()
        self.cronometro.toggleMaximizeRestore()
        self.cronometro.showMaximized.assert_called_once()  # Debería llamar a showMaximized

        self.cronometro.isMaximized = MagicMock(return_value=True)
        self.cronometro.toggleMaximizeRestore()
        self.cronometro.showNormal.assert_called_once()  # Debería llamar a showNormal

if __name__ == '__main__':
    unittest.main()
