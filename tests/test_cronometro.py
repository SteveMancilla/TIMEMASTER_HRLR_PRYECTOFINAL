import unittest
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from Cronometro import Cronometro
from src.modelo.db import DB, TimerModel, UsuarioModel

class TestCronometro(unittest.TestCase):

    def setUp(self):
        # Configurar una aplicación PyQt5 para las pruebas
        self.app = QApplication([])
        self.cronometro = Cronometro()
        self.base = DB()
        # Mockear la sesión de la base de datos
        self.mock_session = MagicMock()
        self.cronometro.db.get_session=MagicMock(return_value=self.mock_session)

    def test_guardar_minutos(self):
        # Simular la selección de minutos y la acción de guardar
        self.cronometro.cbMinutosTrabajoCrono.setCurrentText("25")
        self.cronometro.guardarminutos()

        # Verificar que se haya llamado a add en la sesión simulada
        self.assertFalse(self.mock_session.add.called)
        added_instance = self.mock_session.add.call_args[0][0]
        self.assertIsInstance(added_instance, TimerModel)

        # Verificar que se haya llamado a commit en la sesión simulada
        self.assertFalse(self.mock_session.commit.called)

    def test_guardar_segundos(self):
        # Simular la selección de segundos y la acción de guardar
        self.cronometro.cbMinutosTrabajoCrono.setCurrentText("5")
        self.cronometro.guardarseg()

        # Verificar que se haya llamado a add en la sesión simulada
        self.assertTrue(self.mock_session.add.called)
        added_instance = self.mock_session.add.call_args[0][0]
        self.assertIsInstance(added_instance, TimerModel)

        # Verificar que se haya llamado a commit en la sesión simulada
        self.assertTrue(self.mock_session.commit.called)


    def tearDown(self):
        # Limpiar después de las pruebas
        self.cronometro.session.close()
        self.cronometro.db.close()
        self.app.quit()

if __name__ == '__main__':
    unittest.main()

