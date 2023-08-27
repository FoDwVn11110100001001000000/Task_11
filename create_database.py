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

def fetch(column, table):
    with sqlite3.connect('my_data.db') as con:
        cur = con.cursor()
        cur.execute(f"SELECT DISTINCT {column} FROM {table};")
        results = cur.fetchall()
        list_names = [result[0] for result in results]
        return len(list_names)
    

def fill_students():
    sql_command = "\n".join(f"INSERT INTO students (student, group_id) VALUES ('{fake_data.student()}', {random.randint(1, 3)});" for _ in range(30))
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
    students_counter = fetch('student', 'students') + 1
    subjects_counter = fetch('subj', 'subjects') + 1

    sql_commands = list()

    for s in range(1, students_counter):
        num_grades = random.randint(10, 20)
        for _ in range(num_grades):
            subject_id = random.randint(1, subjects_counter)
            grade_date = fake_data.date()

            sql_command = f"""
                INSERT INTO grades (student_id, subject_id, grade, grade_date) 
                VALUES ({s}, {subject_id}, '{fake_data.grade()}', '{grade_date}');
            """
            sql_commands.append(sql_command)
    connector("\n".join(sql_commands))


if __name__ == "__main__":
    create_db()
    fill_students()
    fill_teachers()
    fill_groups()
    fill_subjects()
    fill_grades()