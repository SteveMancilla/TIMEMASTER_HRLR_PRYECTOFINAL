from db import DB

class Timer:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.id = None

    def save(self):
        db = DB("timemaster.db")
        db.insert("timers", [self.name, self.duration])
        self.id = db.cursor.lastrowid
        db.close()

    def load(self, id):
        db = DB("timemaster.db")
        db.cursor.execute("SELECT * FROM timers WHERE id = ?", (id,))
        row = db.cursor.fetchone()
        self.name = row[1]
        self.duration = row[2]
        db.close()