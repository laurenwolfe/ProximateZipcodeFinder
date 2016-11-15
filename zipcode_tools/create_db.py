import sqlite3


class ZipcodeImporter:
    def __init__(self, filepath, db_name):
        self.in_file = filepath
        self.db_name = db_name

    def create_db(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("CREATE TABLE zipcodes \
              (zipcode INT PRIMARY KEY, \
              latitude DOUBLE, \
              longitude DOUBLE)")
        conn.close()

    def insert_data(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        f = open(self.filepath, 'r')

        for line in f:
            row = line.split("\t")
            c.execute("INSERT INTO zipcodes VALUES (" + row[0] + ", " + row[5] + ", " + row[6] + ")")

        f.close()
        conn.close()

    def clear_data(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM zipcodes")
        conn.close()
