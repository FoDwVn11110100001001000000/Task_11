import fake_data


tables = [
    {
        'name': 'students',
        'data': fake_data.student(),
        'columns': [
            ('id', 'INTEGER PRIMARY KEY'),
            ('ПІБ', 'TEXT'),
        ]
    },
    {
        'name': 'teachers',
        'data': fake_data.teacher(),
        'columns': [
            ('id', 'INTEGER PRIMARY KEY'),
            ('Викладач', 'TEXT')
        ]
    },
        {
        'name': 'subjects',
        'data': fake_data.subject(),
        'columns': [
            ('id', 'INTEGER PRIMARY KEY'),
            ('Предмет', 'TEXT')
        ]
    },
        {
        'name': 'groups',
        'data': fake_data.group(),
        'columns': [
            ('id', 'INTEGER PRIMARY KEY'),
            ('Група №', 'TEXT')
        ]
    },
        {
        'name': 'grades',
        'data': fake_data.grade(),
        'columns': [
            ('id', 'INTEGER PRIMARY KEY'),
            ('Студент', 'TEXT'),
            ('Оцінка1', 'TEXT'),
            ('Оцінка2', 'TEXT'),
            ('Оцінка3', 'TEXT')
        ]
    }
]