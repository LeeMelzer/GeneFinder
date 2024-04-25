import sqlite3

class Database(object):

    def __init__(self):
        self.connection = sqlite3.connect('storedSequences.db')
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sequences(
                            species text, 
                            gene text,
                            sequence text)''')
        
    def insert_sequences(self, sequences):
        self.cursor.executemany("INSERT INTO sequences VALUES(?,?,?)", sequences)
        
    def get_sequences(self):
        self.cursor.execute('''SELECT * FROM sequences''')
        sequences = self.cursor.fetchall()
        return sequences

    def check_table_exists(self):
        try:
            self.cursor.execute('''SELECT * FROM sequences''')
            sequences = self.cursor.fetchall()
            if len(sequences) != 0:
                return True
        except sqlite3.OperationalError:
            return False