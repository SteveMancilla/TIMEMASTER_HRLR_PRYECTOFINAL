import unittest
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtCore import QTime
from Alarma import Alarma

class TestAlarma(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Necesario para PyQt5

    def setUp(self):
        # Inicializar la instancia de Alarma
        self.alarma = Alarma()

    def test_agregarAlarma(self):
        # Configuración del estado de los campos
        self.alarma.cbHorasAlarma.setCurrentText("15")
        self.alarma.cbMinutosAlarma.setCurrentText("45")
        self.alarma.cbSonido.setCurrentText("Sonido 02")
        self.alarma.txtNombre.setText("Otra Alarma")

        # Llamar al método
        self.alarma.agregarAlarma()

        # Verificar que la fila fue agregada al QTableWidget
        self.assertEqual(self.alarma.tblAlarma.rowCount(), 1)
        item_hora = self.alarma.tblAlarma.item(0, 0)
        item_minuto = self.alarma.tblAlarma.item(0, 1)
        item_sonido = self.alarma.tblAlarma.item(0, 2)
        item_nombre = self.alarma.tblAlarma.item(0, 3)
        self.assertEqual(item_hora.text(), "15")
        self.assertEqual(item_minuto.text(), "45")
        self.assertEqual(item_sonido.text(), "Sonido 02")
        self.assertEqual(item_nombre.text(), "Otra Alarma")

    def test_cargarDatosSeleccionados(self):
        # Simular una fila seleccionada en el QTableWidget
        self.alarma.tblAlarma.insertRow(0)
        self.alarma.tblAlarma.setItem(0, 0, QTableWidgetItem("14"))
        self.alarma.tblAlarma.setItem(0, 1, QTableWidgetItem("35"))
        self.alarma.tblAlarma.setItem(0, 2, QTableWidgetItem("Sonido 03"))
        self.alarma.tblAlarma.setItem(0, 3, QTableWidgetItem("Alarma Test"))

        self.alarma.tblAlarma.setCurrentCell(0, 0)
        self.alarma.cargarDatosSeleccionados()

        # Verificar que los datos fueron cargados en los campos
        self.assertEqual(self.alarma.cbHorasAlarma.currentText(), "14")
        self.assertEqual(self.alarma.cbMinutosAlarma.currentText(), "35")
        self.assertEqual(self.alarma.cbSonido.currentText(), "Sonido 03")
        self.assertEqual(self.alarma.txtNombre.text(), "Alarma Test")

    def test_calcularTiempoRestante(self):
        # Configurar la hora actual y la hora de la alarma
        self.alarma.cbHorasAlarma.setCurrentText("15")
        self.alarma.cbMinutosAlarma.setCurrentText("30")

        tiempo_restante = self.alarma.calcularTiempoRestante(15, 30)
        hora_actual = QTime.currentTime()
        alarma = QTime(15, 30)

        if alarma < hora_actual:
            diferencia_horas = (24 - hora_actual.hour()) + 15
            diferencia_minutos = 30 - hora_actual.minute()
        else:
            diferencia_horas = 15 - hora_actual.hour()
            diferencia_minutos = 30 - hora_actual.minute()

        if diferencia_minutos < 0:
            diferencia_minutos += 60
            diferencia_horas -= 1

        self.assertEqual(tiempo_restante['horas'], diferencia_horas)
        self.assertEqual(tiempo_restante['minutos'], diferencia_minutos)

if __name__ == '__main__':
    unittest.main()
