# db.py

import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('luminae_bot/data/scores.db') # create a connection to the SQLite database
        print(f'successful connection with sqlite version {sqlite3.version}')
    except Error as e:
        print(f'Error {e} occurred')

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(f'Error {e} occurred')

# the function to execute when the program starts
def main():

    database = r'luminae_bot/data/scores.db'

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS scores (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        score integer,
                                        category text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS asked_questions (
                                    id integer PRIMARY KEY,
                                    question_id text NOT NULL,
                                    category text
                                );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")
        
if __name__ == '__main__':
    main()
