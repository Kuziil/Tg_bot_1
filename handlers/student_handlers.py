from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from keyboards.keyboards_start import user_identifier

student_router: Router = Router()


@student_router.callback_query(Text(text='student'))
async def process_student_press(callback: CallbackQuery):
    """
    Этот хэндлер срабатывает при нажатии кнопки 'Студент' и обрабатывает этот запрос.
    :return: Возвращает новые кнопки заменяя текст над сообщением
    """
    await callback.message.edit_text(
        text='ура',
        reply_markup=user_identifier('еп')
    )
