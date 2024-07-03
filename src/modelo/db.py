#NO BORRAR


from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

Base = declarative_base()

class AuditoriaModel(Base):
    __tablename__ = 'tblAuditoria'
    Auditoria_ID = Column(Integer, primary_key=True, autoincrement=True)
    Usuario_ID = Column(Integer, ForeignKey('tblUsuario.Usuario_ID'))
    accion = Column(String, nullable=True)
    fecha_hora = Column(DateTime, default=datetime.datetime.now)

class UsuarioModel(Base):
    __tablename__ = 'tblUsuario'
    Usuario_ID = Column(Integer, primary_key=True, autoincrement=True)
    Usuario_Nombre = Column(String, nullable=False)
    Usuario_DNI = Column(String, nullable=False)
    #Usuario_Apellido_Paterno = Column(String, nullable=False)
    #Usuario_Celular = Column(String, nullable=False)
    #Usuario_Email = Column(String, nullable=False)
    auditorias = relationship("AuditoriaModel")

class TimerModel(Base):
    __tablename__ = 'tblTemporizador'
    temporizador_ID = Column(Integer, primary_key=True, autoincrement=True)
    temporizador_TiempoMinutos = Column(Float, nullable=True)
    Temporizador_TiempoSegundos = Column(Float, nullable=True)
    #temporizador_estado = Column(String, nullable=False)
    Usuario_ID = Column(Integer, ForeignKey('tblUsuario.Usuario_ID'))
    Auditoria_ID = Column(Integer, ForeignKey('tblAuditoria.Auditoria_ID'))

class AlarmModel(Base):
    __tablename__ = 'tblAlarma'
    Alarma_ID = Column(Integer, primary_key=True, autoincrement=True)
    Alarma_Hora_Programada = Column(Float, nullable=False)
    Alarma_Minuto_Programada = Column(Float, nullable=False)
    Alarma_Sonido = Column(String, nullable=False)
    Alarma_Nombre = Column(String, nullable=False)
    Usuario_ID = Column(Integer, ForeignKey('tblUsuario.Usuario_ID'))
    Auditoria_ID = Column(Integer, ForeignKey('tblAuditoria.Auditoria_ID'))

class PomodoroModel(Base):
    __tablename__ = 'tblTemporizadorPomodoro'
    TemPom_ID = Column(Integer, primary_key=True, autoincrement=True)
    temPom_Duracion_trabajo = Column(Float, nullable=False)
    temPom_Duracion_descanso = Column(Float, nullable=False)
    Usuario_ID = Column(Integer, ForeignKey('tblUsuario.Usuario_ID'))
    Auditoria_ID = Column(Integer, ForeignKey('tblAuditoria.Auditoria_ID'))

class DB:
    def __init__(self, db_name="timemaster.db"):
        self.engine = create_engine(f"sqlite:///{db_name}")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def get_session(self):
        return self.Session()
    
    def close(self):
        self.engine.dispose()
    
    def register_audit(self, session, usuario_id, accion):
        audit = AuditoriaModel(Usuario_ID=usuario_id, accion=accion)
        session.add(audit)
        session.commit()
        return audit