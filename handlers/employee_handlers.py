from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Text
from keyboards.keyboards_for_employee import markup_tel
from aiogram.types import ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_FOR_EMPLOYEE
from config_data.config import Config, load_config

employee_router: Router = Router()

config: Config = load_config()


@employee_router.callback_query(Text(text='employee'))
async def process_employee_press(callback: CallbackQuery):
    """
    Этот хэндлер срабатывает при выборе кнопки 'Сотрудник'.
    :param callback:
    :return: Предлагает отправить номер телефона
    """
    await callback.message.answer(text=LEXICON_FOR_EMPLOYEE['send_tel_up'], reply_markup=markup_tel)


@employee_router.message(F.contact.phone_number.in_(config.tg_bot.employee_contact))
async def process_true_contact(message: Message):
    """
    Этот хэндлер проверяет номер телефона и если он есть в бд, то отвечает Верно.
    :param message:
    :return:
    """
    await message.answer(text=LEXICON_FOR_EMPLOYEE['contact_true'], reply_markup=ReplyKeyboardRemove())


@employee_router.message(F.contact)
async def process_false_contact(message: Message):
    """
    Этот хэндлер отлавливает остальные номера телефона, которых нет в бд.
    :param message:
    :return:
    """

    await message.answer(text=LEXICON_FOR_EMPLOYEE['contact_false'], reply_markup=ReplyKeyboardRemove())
