IN_THE_WORKS: str = ' еще в разработке'
MENU_IN_THE_WORK: str = 'еще не переданы краткие пояснения'
BACK: str = '⬅️Назад'

LEXICON: dict[str, str] = {
    'other_answer': 'Не понимаю, что вы имеете ввиду'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': '<b>Здравствуйте!</b>\n\n'
              'Кем вы являетесь для НГАСУ(Сибстрин)?',
    '/help': '/help' + IN_THE_WORKS
}

LEXICON_COMMANDS_FOR_MENU: dict[str, str] = {
    '/start': MENU_IN_THE_WORK,
    '/help': MENU_IN_THE_WORK
}

LEXICON_FOR_INDICATION: dict[str, str] = {
    'student': '👨‍🎓Студент👩‍🎓',
    'employee': '👨‍🏫Сотрудник👩‍🏫',
}

LEXICON_FOR_STUDENTS: dict[str, str] = {
    'after_start_for_students': 'Выберите интересующий вас раздел:',
    'timetable': '🗓Расписание',
    'what_date': 'Выберете интересующую дату\n\n'
                 '<b>Функция находиться в разработке, все кнопки не активны</b>',
    'order_certificates': '📋Заказ справок',
    'where_to_get_a_student_card': IN_THE_WORKS,
    'what_kind_of_certificates': 'Какую справку требуется заказать?',
    'certificates_1': '📄С места учебы',
    'certificates_2': '📄Копия диплома',
    'certificates_3': '📄Оригинал диплома',
    'back_after_certificates_for_students': BACK,
    'student card': '📄Студенческий билет',
    'back_after_start_for_students': BACK
}

LEXICON_FOR_EMPLOYEE: dict[str, str] = {
    'send_tel': 'Отправь номер телефона',
    'send_tel_up': 'Для авторизации нажмите на появившуюся под строкой ввода кнопку "Отправить номер телефона"📱',
    'contact_true': 'Вы сотрудник',
    'contact_false': 'Вы не сотрудник'
}
