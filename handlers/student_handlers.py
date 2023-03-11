from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from keyboards.keyboards_for_students import main_students_kb
from lexicon.lexicon import LEXICON_FOR_STUDENTS

student_router: Router = Router()


@student_router.callback_query(Text(text='student'))
async def process_student_press(callback: CallbackQuery):
    """
    Этот хэндлер срабатывает при нажатии кнопки 'Студент' и обрабатывает этот запрос.
    :return: Возвращает новые кнопки заменяя текст над сообщением
    """
    await callback.message.edit_text(
        text=LEXICON_FOR_STUDENTS['after_start_for_students'],
        reply_markup=main_students_kb('timetable', 'order_certificates', 'student card')
    )
