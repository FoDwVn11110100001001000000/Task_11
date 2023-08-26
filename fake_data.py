from random import sample, choice, randint

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
    grades = ['A', 'B', 'C', 'D', 'E']

    quantity = randint(1,3)
    grades_str = [choice(grades) for _ in range(quantity)]
    return grades_str

print(grade())