from random import sample, choice, randint

from faker import Faker


fake = Faker('uk_UA')

counter_students = 0
counter_groups = 0
counter_teachers = 0
counter_subjects = 0
counter_grade = 0

def student():
    global counter_students
    students = fake.name()
    counter_students += 1
    return students

def group():
    global counter_groups
    i = randint(1, 100)
    groups = f'BG-{i}'
    counter_groups += 1
    return groups

def teacher():
    global counter_teachers
    list_of_teachers = f'Професор {fake.last_name()}'
    counter_teachers += 1 
    return list_of_teachers

def subject():
    global counter_subjects
    list_of_subjects = [
        "Математика",
        "Українська мова",
        "Література",
        "Історія",
        "Географія",
        "Фізика",
        "Хімія",
        "Біологія",
        "Англійська мова",
        "Французька мова",
        "Іспанська мова",
        "Інформатика",
        "Музика",
        "Образотворче мистецтво",
        "Фізична культура",
    ]
    random_subjects = sample(list_of_subjects, k=7)
    return random_subjects

def date():
    # Поверне список із 50-ти дат
    res = list()
    for _ in range(50):
        past_date = fake.past_date(start_date="-365d")
        date_str = past_date.strftime("%Y-%m-%d")
        res.append(date_str)
    return res

def grade():
    global counter_grade
    # Поверне список із 50-ти оцінок
    grades = ['A', 'B', 'C', 'D', 'E']

    res = list()
    quantity = randint(1,3)
    for _ in range(50):
        list_of_grades = [choice(grades) for _ in range(quantity)]
        res.extend(list_of_grades)
    return res
