-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student VARCHAR(255) UNIQUE NOT NULL
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher VARCHAR(255) UNIQUE NOT NULL
);

-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(255) UNIQUE NOT NULL
);

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subj VARCHAR(255) NOT NULL,
    teacher_name INTEGER,
    FOREIGN KEY (teacher_name) REFERENCES teachers(id)
);

-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    student TEXT,
    subjects TEXT,
    grade TEXT,
    grade_date TEXT,
    FOREIGN KEY (students) REFERENCES student(id)

