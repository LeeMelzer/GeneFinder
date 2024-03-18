import sqlite3

# just an idea, not sure yet what I'm doing with this

class Database(object):

    def __init__(self):
        self.connection = sqlite3.connect('storedSequences.db')
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sequences(species text, \
                                                                    gene text PRIMARY KEY,
                                                                    sequence text)''')
        
    def commit(self):
        self.connection.commit()
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   