from aiogram.types import CallbackQuery
from aiogram import Router

from keyboards.keyboards_for_students import main_students_kb
from lexicon.lexicon import LEXICON_FOR_API
from resources.API import response

api_router: Router = Router()


@api_router.callback_query(
    lambda x: True if x.data == 'back_after_certificates_for_students' or x.data == 'test_api' else False)
async def process_api_press(callback: CallbackQuery):
    """
    Этот хэндлер срабатывает при нажатии кнопки 'Овощи?' и обрабатывает этот запрос.
    Также является обработчиком кнопки назад.
    :return: Возвращает новые кнопки заменяя текст над сообщением и новые кнопки
    """
    await callback.message.edit_text(
        text=LEXICON_FOR_API['after_start_for_api'],
        reply_markup=main_students_kb(*[response[x]['name'] for x in range(len(response))])
    )
