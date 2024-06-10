
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DB:
    def __init__(self, db_name):
        self.engine = create_engine("sqlite:///{db_name}")
        self.Session = sessionmaker(bind=self.engine)
    
    def create_table(self, table_name, columns):
        self.engine.execute("CREAR LA TANBLA SI NO EXISTE {table_name} ({columns})")
    
    def insert(self, table_name, values):
        session = self.Session()
        session.add_all(values)
        session.commit()
        session.close()

    def select(self, table_name, columns):
        session = self.Session()
        result = session.query(table_name).all()
        session.close()
        return result

    def close(self):
        self.engine.dispose()