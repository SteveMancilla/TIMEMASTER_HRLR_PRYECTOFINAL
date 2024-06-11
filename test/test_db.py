import unittest
from src.modelo.db import DB, TimerModel, AlarmModel, PomodoroModel, UsuarioModel, AuditoriaModel
from datetime import datetime

class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = DB(":memory:")
        self.session = self.db.get_session()

    def tearDown(self):
        self.session.close()
        self.db.close()

    def test_insert_usuario(self):
        usuario = UsuarioModel(
            Usuario_Nombre="Test",
            Usuario_Apellido_Paterno="User",
            Usuario_Celular="1234567890",
            Usuario_Email="test@example.com"
        )
        self.session.add(usuario)
        self.session.commit()
        self.assertIsNotNone(usuario.Usuario_ID)

    def test_insert_timer(self):
        usuario = UsuarioModel(
            Usuario_Nombre="Test",
            Usuario_Apellido_Paterno="User",
            Usuario_Celular="1234567890",
            Usuario_Email="test@example.com"
        )
        self.session.add(usuario)
        self.session.commit()
        audit = self.db.register_audit(self.session, usuario.Usuario_ID, 'Iniciar temporizador')

        timer = TimerModel(
            temporizador_Tiempo=60, 
            temporizador_estado='Iniciado',
            Usuario_ID=usuario.Usuario_ID,
            Auditoria_ID=audit.Auditoria_ID
        )
        self.session.add(timer)
        self.session.commit()
        self.assertIsNotNone(timer.temporizador_ID)

    def test_insert_alarm(self):
        usuario = UsuarioModel(
            Usuario_Nombre="Test",
            Usuario_Apellido_Paterno="User",
            Usuario_Celular="1234567890",
            Usuario_Email="test@example.com"
        )
        self.session.add(usuario)
        self.session.commit()
        audit = self.db.register_audit(self.session, usuario.Usuario_ID, 'Configurar alarma')

        alarm_time = datetime.now()
        alarm = AlarmModel(
            Alarma_Hora_Programada=alarm_time, 
            Alarma_Estado='Programada',
            Usuario_ID=usuario.Usuario_ID,
            Auditoria_ID=audit.Auditoria_ID
        )
        self.session.add(alarm)
        self.session.commit()
        self.assertIsNotNone(alarm.Alarma_ID)

    def test_insert_pomodoro(self):
        usuario = UsuarioModel(
            Usuario_Nombre="Test",
            Usuario_Apellido_Paterno="User",
            Usuario_Celular="1234567890",
            Usuario_Email="test@example.com"
        )
        self.session.add(usuario)
        self.session.commit()
        audit = self.db.register_audit(self.session, usuario.Usuario_ID, 'Iniciar pomodoro')

        pomodoro = PomodoroModel(
            temPom_Duracion_trabajo=25, 
            temPom_Duracion_descanso=5,
            Usuario_ID=usuario.Usuario_ID,
            Auditoria_ID=audit.Auditoria_ID
        )
        self.session.add(pomodoro)
        self.session.commit()
        self.assertIsNotNone(pomodoro.TemPom_ID)

if __name__ == "__main__":
    unittest.main()
