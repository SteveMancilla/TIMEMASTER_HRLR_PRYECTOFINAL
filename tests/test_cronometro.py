import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QApplication
from Cronometro import Cronometro
from src.modelo.db import DB, UsuarioModel, TimerModel

class TestCronometro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Necesario para PyQt5

    def setUp(self):
        # Mock de la base de datos
        self.db_patch = patch('src.vista.Cronometro.DB', autospec=True)
        self.mock_db = self.db_patch.start()
        
        # Mock de la sesión
        self.mock_session = MagicMock()
        self.mock_db.return_value.get_session.return_value = self.mock_session
        
        # Mock del usuario
        self.mock_usuario = UsuarioModel(Usuario_ID=1, Usuario_Nombre="Test User", Usuario_DNI="12345678")
        self.mock_session.query.return_value.order_by.return_value.first.return_value = self.mock_usuario

        # Inicializar la instancia de Cronometro
        self.cronometro = Cronometro()

    def tearDown(self):
        self.db_patch.stop()

    def test_guardarminutos(self):
        self.cronometro.cbMinutosTrabajoCrono.setCurrentText("25")
        self.cronometro.cbMinDescansoCrono.setCurrentText("5")
        self.cronometro.guardarminutos()

        self.mock_session.add.assert_called_once()
        self.mock_session.commit.assert_called_once()

        added_timer = self.mock_session.add.call_args[0][0]
        self.assertEqual(added_timer.temporizador_TiempoMinutos, 25)
        self.assertEqual(added_timer.Temporizador_TiempoSegundos, 5)
        self.assertEqual(added_timer.Usuario_ID, 1)

    def test_guardarseg(self):
        self.cronometro.cbMinutosTrabajoCrono.setCurrentText("25")
        self.cronometro.cbMinDescansoCrono.setCurrentText("5")
        self.cronometro.guardarseg()

        self.mock_session.add.assert_called_once()
        self.mock_session.commit.assert_called_once()

        added_timer = self.mock_session.add.call_args[0][0]
        self.assertEqual(added_timer.temporizador_TiempoMinutos, 25)
        self.assertEqual(added_timer.Temporizador_TiempoSegundos, 5)

if __name__ == '__main__':
    unittest.main()
