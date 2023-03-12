from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup
from lexicon.lexicon import LEXICON_FOR_EMPLOYEE

button_tel: KeyboardButton = KeyboardButton(text=LEXICON_FOR_EMPLOYEE['send_tel'], request_contact=True)
markup_tel: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button_tel]], resize_keyboard=True, one_time_keyboard=True)
