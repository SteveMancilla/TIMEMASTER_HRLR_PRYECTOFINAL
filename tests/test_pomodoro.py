import unittest
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication  # Importar QApplication

# Importar la clase Pomodoro desde pomodoro.py
from Pomodoro import Pomodoro

class TestPomodoro(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializar una aplicación Qt en modo headless para las pruebas
        cls.app = QApplication([])

    @classmethod
    def tearDownClass(cls):
        # Cerrar la aplicación Qt después de que todas las pruebas hayan terminado
        cls.app.exit()

    def setUp(self):
        # Configurar mock para la sesión de la base de datos
        self.mock_session = MagicMock()
        self.db = MagicMock()
        self.db.get_session = MagicMock(return_value=self.mock_session)

        # Crear instancia de Pomodoro sin inicializar la GUI completa
        self.pomodoro = Pomodoro()

    def test_guardar_pomodoro_db(self):
        # Simular usuario obtenido de la base de datos
        usuario_mock = MagicMock()
        usuario_mock.Usuario_ID = 1
        self.mock_session.query.return_value.order_by.return_value.first.return_value = usuario_mock

        # Simular selección de tiempos de trabajo y descanso
        self.pomodoro.cbMinutosTrabajoPom.setCurrentText("25")
        self.pomodoro.cbMinDescansoPom.setCurrentText("5")

        # Ejecutar método para guardar configuración en la base de datos
        self.pomodoro.guardarPomoDB()

        # Verificar que se llamó a add en la sesión simulada
        self.assertTrue(self.mock_session.add.called)
        added_instance = self.mock_session.add.call_args[0][0]
        self.assertIsInstance(added_instance, MagicMock)

        # Verificar que se llamó a commit en la sesión simulada
        self.assertTrue(self.mock_session.commit.called)

    def test_guardar_pomodoro_db_no_usuario(self):
        # Simular que no se encuentra ningún usuario registrado
        self.mock_session.query.return_value.order_by.return_value.first.return_value = None

        # Ejecutar método para guardar configuración en la base de datos
        self.pomodoro.guardarPomoDB()

        # Verificar que no se llamó a add ni a commit porque no hay usuario registrado
        self.assertFalse(self.mock_session.add.called)
        self.assertFalse(self.mock_session.commit.called)

    def tearDown(self):
        # Limpiar recursos después de cada prueba si es necesario
        pass

if __name__ == "__main__":
    unittest.main()
