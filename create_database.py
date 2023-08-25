import random
import sqlite3

import fake_data

def connector(sql):
    with sqlite3.connect('my_data.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

def create_db():
    with open('database.sql', 'r') as f:
        sql = f.read()
    
    connector(sql)

def fill_students():
    randomise = random.randint(30,50)
    sql_command = "\n".join(f"INSERT INTO students (student) VALUES ('{fake_data.student()}');" for _ in range(randomise))
    connector(sql_command)

def fill_teachers():
    randomise = random.randint(3,5)
    sql_command = "\n".join(f"INSERT INTO teachers (teacher) VALUES ('{fake_data.teacher()}');" for _ in range(randomise))
    connector(sql_command)

def fill_groups():
    sql_command = "\n".join(f"INSERT INTO groups (group_name) VALUES ('{fake_data.group()}');" for _ in range(3))
    connector(sql_command)

if __name__ == "__main__":
    create_db()
    fill_students()
    fill_teachers()
    fill_groups()