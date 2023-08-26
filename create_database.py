import random
import sqlite3

import fake_data

teachers_list = []

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
    global teachers_list
    randomise = random.randint(3,5)
    teachers_list = [fake_data.teacher() for _ in range(randomise)]
    sql_command = "\n".join(f"INSERT INTO teachers (teacher) VALUES ('{teacher}');" for teacher in teachers_list)
    connector(sql_command)

def fill_groups():
    sql_command = "\n".join(f"INSERT INTO groups (group_name) VALUES ('{fake_data.group()}');" for _ in range(3))
    connector(sql_command)

def fill_subjects():
    global teachers_list
    randomise = random.randint(5, 8)
    subj_list = [ (fake_data.subject(), random.choice(teachers_list)) for _ in range(randomise)]
    sql_command = "\n".join(f"INSERT INTO subjects (subj, teacher_name) VALUES {subj};" for subj in subj_list)
    connector(sql_command)

def fill_grades():
    randomise = random.randint(1, 3)
    subj_list = [ (fake_data.subject(), random.choice(teachers_list)) for _ in range(randomise)]
    sql_command = "\n".join(f"INSERT INTO grades (student, subjects, grade, grade_date) VALUES {subj};" for subj in subj_list)
    print(sql_command)

    
if __name__ == "__main__":
    create_db()
    fill_students()
    fill_teachers()
    fill_groups()
    fill_subjects()
    fill_grades()