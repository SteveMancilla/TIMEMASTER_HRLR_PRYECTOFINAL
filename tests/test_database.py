import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.db import Base, DB, UsuarioModel, AuditoriaModel, TimerModel, PomodoroModel
import datetime

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Crear una base de datos en memoria para las pruebas
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        cls.db = DB(db_name=":memory:")

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        cls.db.close()

    def setUp(self):
        self.session = self.db.get_session()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_create_user(self):
        user = UsuarioModel(Usuario_Nombre="Juan Perez", Usuario_DNI="12345678")
        self.session.add(user)
        self.session.commit()
        
        retrieved_user = self.session.query(UsuarioModel).filter_by(Usuario_Nombre="Juan Perez").first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.Usuario_Nombre, "Juan Perez")

    def test_register_audit(self):
        user = UsuarioModel(Usuario_Nombre="Juan Perez", Usuario_DNI="12345678")
        self.session.add(user)
        self.session.commit()
        
        audit = self.db.register_audit(self.session, user.Usuario_ID, "login")
        
        retrieved_audit = self.session.query(AuditoriaModel).filter_by(Usuario_ID=user.Usuario_ID).first()
        self.assertIsNotNone(retrieved_audit)
        self.assertEqual(retrieved_audit.accion, "login")

    def test_create_timer(self):
        user = UsuarioModel(Usuario_Nombre="Juan Perez", Usuario_DNI="12345678")
        self.session.add(user)
        self.session.commit()
        
        timer = TimerModel(temporizador_TiempoMinutos=25, Temporizador_TiempoSegundos=0, Usuario_ID=user.Usuario_ID)
        self.session.add(timer)
        self.session.commit()
        
        retrieved_timer = self.session.query(TimerModel).filter_by(Usuario_ID=user.Usuario_ID).first()
        self.assertIsNotNone(retrieved_timer)
        self.assertEqual(retrieved_timer.temporizador_TiempoMinutos, 25)

    def test_create_pomodoro(self):
        user = UsuarioModel(Usuario_Nombre="Juan Perez", Usuario_DNI="12345678")
        self.session.add(user)
        self.session.commit()
        
        pomodoro = PomodoroModel(temPom_Duracion_trabajo=25, temPom_Duracion_descanso=5, Usuario_ID=user.Usuario_ID)
        self.session.add(pomodoro)
        self.session.commit()
        
        retrieved_pomodoro = self.session.query(PomodoroModel).filter_by(Usuario_ID=user.Usuario_ID).first()
        self.assertIsNotNone(retrieved_pomodoro)
        self.assertEqual(retrieved_pomodoro.temPom_Duracion_trabajo, 25)
        self.assertEqual(retrieved_pomodoro.temPom_Duracion_descanso, 5)

if __name__ == "__main__":
    unittest.main()
