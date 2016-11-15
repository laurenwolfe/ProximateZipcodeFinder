"""
Creates a database of US zipcodes and their center coordinates.
Also provides a query runner utility, reducing redundancy. Note that this
isn't sanitizing input; in this case it's not a problem because I'm the
only client of the code, but it would be unwise to do this when interacting with
user inputs.
"""

import sqlite3

class Database:
    """
    filepath: path to file, may be left blank if not inserting data from a file.
    db_name: name of sqlite database
    """
    def __init__(self, filepath, db_name):
        self.filepath = filepath
        self.db_name = db_name

    '''
    Creates the zipcode database table.
    '''
    def create_db(self):
        query = "CREATE TABLE IF NOT EXISTS zipcodes \
              (zipcode INT PRIMARY KEY, \
              latitude DOUBLE, \
              longitude DOUBLE)"
        self.run_query(query)

    '''
    Concatenates insert rows into one query;
    It works fine for this dataset, but if it were larger I'd need to be
    careful not to run out of memory (batch processing)
    '''
    def insert_data(self):
        query = "INSERT INTO zipcodes VALUES "

        try:
            with open(self.filepath) as f:
                # skip header row
                next(f)
                for line in f:
                    row = line.split("\t")
                    query += "(" + row[0] + ", " + row[5] + ", " + row[6] + "),"
            # remove last comma
            query = query[:-1]
            self.run_query(query)

            f.close()
        except IOError:
            print "Filepath " + self.filepath + " is invalid; insert failed."

    '''
    Connects and runs query passed as an argument, returning results, if any,
    as a list of tuples (each representing selected fields for a single row).
    Here's another place with the potential for running out of memory.
    '''
    def run_query(self, query):
        if self.db_name == "":
            print "No database name provided on instantiation"
            return
        else:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            try:
                c.execute(query)
                rows = c.fetchall()
                conn.commit()
            except sqlite3.Error as e:
                print "Sqlite3 error: " + e.args[0]
                return

        conn.close()
        return rows
