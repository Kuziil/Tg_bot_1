from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from keyboards.keyboards_for_students import main_students_kb
from lexicon.lexicon import LEXICON_FOR_STUDENTS

student_router: Router = Router()


@student_router.callback_query(
    lambda x: True if x.data == 'back_after_certificates_for_students' or x.data == 'student' else False)
async def process_student_press(callback: CallbackQuery):
    """
    Этот хэндлер срабатывает при нажатии кнопки 'Студент' и обрабатывает этот запрос.
    :return: Возвращает новые кнопки заменяя текст над сообщением и новые кнопки
    """
    await callback.message.edit_text(
        text=LEXICON_FOR_STUDENTS['after_start_for_students'],
        reply_markup=main_students_kb('timetable', 'order_certificates', 'student card',
                                      'back_after_start_for_students')
    )


@student_router.callback_query(Text(text='order_certificates'))
async def process_order_certificates_push(callback: CallbackQuery):
    """
    Этот хэндлер срабатывает при нажатии кнопки 'Заказ справок' и обрабатывает этот запрос.
    :return: Предлагает выбрать интересующие справки
    """
    print(callback, sep='\n')
    await callback.message.edit_text(
        text=LEXICON_FOR_STUDENTS['what_kind_of_certificates'],
        reply_markup=main_students_kb('certificates_1', 'certificates_2', 'certificates_3',
                                      'back_after_certificates_for_students'))
