from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text

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
        reply_markup=main_students_kb(*[response[x]['name'] for x in range(len(response))],
                                      'back_after_start_for_students')
    )


@api_router.callback_query(Text(text=response[0]['name']))
async def process_select_response_0(callback: CallbackQuery):
    """
    Этот хэндлер срабатывает при нажатии кнопки 'Заказ справок' и обрабатывает этот запрос.
    :return: Предлагает выбрать интересующие справки
    """
    serial_number = 0
    await callback.message.edit_text(
        text=f"Штрих-код: {response[serial_number]['barcode']}\n"
             f"Код: {response[serial_number]['cod']}\n"
             f"Артикул: {response[serial_number]['articul']} ",
    )
