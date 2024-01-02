import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, '
                          'category INTEGER NOT NULL, data1 FLOAT NOT NULL, data2 FLOAT NOT NULL)')
        self.conn.commit()

    def get_record(self, record_id):
        cursor = self.conn.execute('SELECT * FROM data WHERE id = ?', (record_id,))
        row = cursor.fetchone()
        if row is None:
            return {}
        return dict(row)

    def get_records(self):
        cursor = self.conn.execute('SELECT * FROM data')
        rows = cursor.fetchall()
        if rows is None:
            return []
        return [dict(row) for row in rows]

    def add_record(self, category, data1, data2):
        cursor = self.conn.execute('INSERT INTO data (category, data1, data2) VALUES (?, ?, ?)', (category, data1, data2))
        self.conn.commit()
        return cursor.lastrowid

    def delete_record(self, record_id):
        self.conn.execute('DELETE FROM data WHERE id = ?', (record_id,))
        self.conn.commit()
        return record_id

    def update_record(self, record_id, category, data1, data2):
        self.conn.execute('UPDATE data SET category = ?, data1 = ?, data2 = ? WHERE id = ?',
                          (category, data1, data2, record_id))
        self.conn.commit()

    def close(self):
        self.conn.close()
