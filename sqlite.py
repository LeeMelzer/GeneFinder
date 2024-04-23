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
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sequences(species text, \
                                                                    gene text PRIMARY KEY,
                                                                    sequence text)''')
        
    def insert_sequences(self):
        # open file and ierate ?
        self.cursor.execute('''INSERT INTO sequences VALUES (species, gene, sequence)''')
        
    def get_sequences(self):
        sequences = self.cursor.execute('''SELECT * FROM sequences''')
        return sequences
