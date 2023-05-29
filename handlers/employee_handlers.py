from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Text
from keyboards.keyboards_for_employee import markup_tel
from aiogram.types import ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_FOR_EMPLOYEE

employee_router: Router = Router()


@employee_router.callback_query(Text(text='employee'))
async def process_employee_press(callback: CallbackQuery):
    """
    Этот хэндлер срабатывает при выборе кнопки 'Сотрудник'.
    :param callback:
    :return: Предлагает отправить номер телефона
    """
    await callback.message.answer(text=LEXICON_FOR_EMPLOYEE['send_tel_up'], reply_markup=markup_tel)


@employee_router.message(F.contact.phone_number.in_(['89137263886', '79137263886', '+79137263886']))
async def process_true_contact(message: Message):
    """
    Этот хэндлер проверяет номер телефона и если он есть в бд, то отвечает Верно.
    На данный момент номера хранятся прямо в фильтре
    !!! Важно дублировать номера в таком формате (+7, 7, 8).
    Это связанно с тем, что иногда настольная и мобильная версия предоставляет номер в разных форматах!!!
    :param message:
    :return:
    """
    print(message.contact)
    await message.answer(text=LEXICON_FOR_EMPLOYEE['contact_true'], reply_markup=ReplyKeyboardRemove())


@employee_router.message(F.contact)
async def process_false_contact(message: Message):
    """
    Этот хэндлер отлавливает остальные номера телефона, которых нет в бд.
    :param message:
    :return:
    """
    await message.answer(text=LEXICON_FOR_EMPLOYEE['contact_false'], reply_markup=ReplyKeyboardRemove())
