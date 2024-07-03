import unittest
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtCore import QTime
from Alarma import Alarma  # Asegúrate de que el archivo se llame Alarma.py

class TestAlarma(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Necesario para PyQt5

    def setUp(self):
        # Inicializar la instancia de Alarma
        self.alarma = Alarma()

        # Configuración inicial para los campos de la alarma
        self.alarma.cbHorasAlarma.setCurrentText("20")
        self.alarma.cbMinutosAlarma.setCurrentText("40")
        self.alarma.cbSonido.setCurrentText("Sonido 01")
        self.alarma.txtNombre.setText("Alarma de Test")

    def test_agregar_alarma(self):
        """Verifica que se agrega una nueva alarma a la tabla con los valores correctos."""
        self.alarma.agregarAlarma()

        # Verificar que la fila fue agregada al QTableWidget
        self.assertEqual(self.alarma.tblAlarma.rowCount(), 1)
        item_hora = self.alarma.tblAlarma.item(0, 0)
        item_minuto = self.alarma.tblAlarma.item(0, 1)
        item_sonido = self.alarma.tblAlarma.item(0, 2)
        item_nombre = self.alarma.tblAlarma.item(0, 3)
        self.assertEqual(item_hora.text(), "20")
        self.assertEqual(item_minuto.text(), "40")
        self.assertEqual(item_sonido.text(), "Sonido 01")
        self.assertEqual(item_nombre.text(), "Alarma de Test")

    def test_cargar_datos_seleccionados(self):
        """Verifica que los datos de una fila seleccionada se cargan en los campos de edición."""
        # Simular una fila seleccionada en el QTableWidget
        self.alarma.tblAlarma.insertRow(0)
        self.alarma.tblAlarma.setItem(0, 0, QTableWidgetItem("18"))
        self.alarma.tblAlarma.setItem(0, 1, QTableWidgetItem("25"))
        self.alarma.tblAlarma.setItem(0, 2, QTableWidgetItem("Sonido 02"))
        self.alarma.tblAlarma.setItem(0, 3, QTableWidgetItem("Otra Alarma"))

        self.alarma.tblAlarma.setCurrentCell(0, 0)
        self.alarma.cargarDatosSeleccionados()

        # Verificar que los datos fueron cargados en los campos
        self.assertEqual(self.alarma.cbHorasAlarma.currentText(), "18")
        self.assertEqual(self.alarma.cbMinutosAlarma.currentText(), "25")
        self.assertEqual(self.alarma.cbSonido.currentText(), "Sonido 02")
        self.assertEqual(self.alarma.txtNombre.text(), "Otra Alarma")

    def test_calcular_tiempo_restante(self):
        """Verifica que se calcula el tiempo restante hasta la alarma correctamente."""
        # Configurar la hora actual y la hora de la alarma
        self.alarma.cbHorasAlarma.setCurrentText("20")
        self.alarma.cbMinutosAlarma.setCurrentText("40")

        with patch('Alarma.QTime.currentTime') as mock_time:
            mock_time.return_value = QTime(18, 30)  # Hora actual simulada

            tiempo_restante = self.alarma.calcularTiempoRestante(20, 40)

            alarma = QTime(20, 40)
            hora_actual = mock_time.return_value

            diferencia_horas = alarma.hour() - hora_actual.hour()
            diferencia_minutos = alarma.minute() - hora_actual.minute()

            if diferencia_minutos < 0:
                diferencia_minutos += 60
                diferencia_horas -= 1

            self.assertEqual(tiempo_restante['horas'], diferencia_horas)
            self.assertEqual(tiempo_restante['minutos'], diferencia_minutos)

    def test_calcular_tiempo_restante_con_hora_menor(self):
        """Verifica que se calcula el tiempo restante correctamente cuando la hora de la alarma es menor que la hora actual."""
        # Configurar la hora actual y la hora de la alarma
        self.alarma.cbHorasAlarma.setCurrentText("00")
        self.alarma.cbMinutosAlarma.setCurrentText("10")

        with patch('Alarma.QTime.currentTime') as mock_time:
            mock_time.return_value = QTime(23, 50)  # Hora actual simulada

            tiempo_restante = self.alarma.calcularTiempoRestante(0, 10)

            alarma = QTime(0, 10)
            hora_actual = mock_time.return_value

            diferencia_horas = (24 - hora_actual.hour()) + alarma.hour()
            diferencia_minutos = alarma.minute() - hora_actual.minute()

            if diferencia_minutos < 0:
                diferencia_minutos += 60
                diferencia_horas -= 1

            self.assertEqual(tiempo_restante['horas'], diferencia_horas)
            self.assertEqual(tiempo_restante['minutos'], diferencia_minutos)

if __name__ == '__main__':
    unittest.main()

