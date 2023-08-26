# Запит 1: Знайти 5 студентів із найбільшим середнім балом з усіх предметів
query_1 = '''
SELECT students.name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY avg_grade DESC
LIMIT 5;
'''

# Запит 2: Знайти студента із найвищим середнім балом з певного предмета
query_2 = '''
SELECT students.name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = ? -- Вставте ID предмета
GROUP BY students.id
ORDER BY avg_grade DESC
LIMIT 1;
'''

# Запит 3: Знайти середній бал у групах з певного предмета
query_3 = '''
SELECT groups.name, AVG(grades.grade) AS avg_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = ? -- Вставте ID предмета
GROUP BY groups.id;
'''

# Запит 4: Знайти середній бал на потоці
query_4 = '''
SELECT AVG(grades.grade) AS avg_grade
FROM grades;
'''

# Запит 5: Знайти, які курси читає певний викладач
query_5 = '''
SELECT subjects.name
FROM subjects
WHERE subjects.teacher_id = ? -- Вставте ID викладача
'''

# Запит 6: Знайти список студентів у певній групі
query_6 = '''
SELECT students.name
FROM students
WHERE students.group_id = ? -- Вставте ID групи
'''

# Запит 7: Знайти оцінки студентів в окремій групі з певного предмета
query_7 = '''
SELECT students.name, grades.grade, grades.grade_date
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = ? -- Вставте ID групи
AND grades.subject_id = ? -- Вставте ID предмета
'''

# Запит 8: Знайти середній бал, який ставить певний викладач зі своїх предметів
query_8 = '''
SELECT AVG(grades.grade) AS avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.teacher_id = ? -- Вставте ID викладача
'''

# Запит 9: Знайти список курсів, які відвідує студент
query_9 = '''
SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = ? -- Вставте ID студента
'''

# Запит 10: Список курсів, які певному студенту читає певний викладач
query_10 = '''
SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.name = ? -- Вставте ім'я студента
AND subjects.teacher_id = ? -- Вставте ID викладача
'''

# Збереження запитів у відповідних файлах
with open('query_1.sql', 'w') as file:
    file.write(query_1)

# Повторіть цей процес для інших запитів (query_2.sql, query_3.sql і т. д.)
