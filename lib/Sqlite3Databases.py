from config import Config
import sqlite3


class Sqlite3Database:
    db = None

    def __init__(self, db_str="test.db") -> None:
        self.db = sqlite3.connect(Config.DBS_DIR + db_str)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def fetchAll(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor.fetchall()

    def fetchOne(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor.fetchone()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        # self.db.close()

    def close(self) -> None:
        self.db.close()
