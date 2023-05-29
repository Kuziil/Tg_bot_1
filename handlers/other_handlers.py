from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON

router: Router = Router()


@router.message()
async def send_other_answer(message: Message):
    """
    Этот хэндлер срабатывает если апдейт пользователя не попал в другие хандлеры:
    ответ на не корректный ввод данных со стороны пользователя
    :return: LEXICON['other_answer']
    """
    await message.answer(text=LEXICON['other_answer'])
