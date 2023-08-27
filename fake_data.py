from random import choice, randint

from faker import Faker


fake = Faker('uk_UA')

def student():
    students = fake.name()
    return students

def group():
    i = randint(1, 100)
    groups = f'BG-{i}'
    return groups

def teacher():
    list_of_teachers = f'Професор {fake.last_name()}'
    return list_of_teachers

def subject():
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
    random_subject = choice(list_of_subjects)
    return random_subject

def date():
    past_date = fake.past_date(start_date="-365d")
    date_str = past_date.strftime("%Y-%m-%d")
    return date_str

def grade():
    grades = [ 1, 2, 3, 4, 5 ]
    grades_str = choice(grades)
    return grades_str
