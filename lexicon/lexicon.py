IN_THE_WORKS: str = ' еще в разработке'
MENU_IN_THE_WORK: str = 'еще не переданы краткие пояснения'
BACK: str = 'Назад'

LEXICON: dict[str, str] = {
    'other_answer': 'Не понимаю, что вы имеете ввиду'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': '/start' + IN_THE_WORKS,
    '/help': '/help' + IN_THE_WORKS
}

LEXICON_COMMANDS_FOR_MENU: dict[str, str] = {
    '/start': MENU_IN_THE_WORK,
    '/help': MENU_IN_THE_WORK
}

LEXICON_FOR_INDICATION: dict[str, str] = {
    'student': 'Студент',
    'employee': 'Сотрудник',
}

LEXICON_FOR_STUDENTS: dict[str, str] = {
    'after_start_for_students': 'Выберите интересующий вас раздел:',
    'timetable': 'Расписание',
    'order_certificates': 'Заказ справок',
    'what_kind_of_certificates': 'Какую справку требуется заказать?',
    'certificates_1': 'С места учебы',
    'certificates_2': 'Копия диплома',
    'certificates_3': 'Оригинал диплома',
    'back_after_certificates_for_students': BACK + '1',
    'student card': 'Студенческий билет',
    'back_after_start_for_students': BACK
}

LEXICON_FOR_USERS: dict[str, str] = {

}
