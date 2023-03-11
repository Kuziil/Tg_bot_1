from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_FOR_STUDENTS


def main_students_kb(*buttons: str) -> InlineKeyboardMarkup:
    """
    Основная клавиатура для ветки студентов
    :param buttons: кнопки по ключу из LEXICON_FOR_STUDENTS.
    :return:  Инлайн клавиатуру с кнопками друг под другом, и последней кнопкой 'Назад'.
    """
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for button in buttons:
        kb_builder.row(InlineKeyboardButton(
            text=LEXICON_FOR_STUDENTS[button] if button in LEXICON_FOR_STUDENTS else
            button, callback_data=button))
    return kb_builder.as_markup()
