from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_FOR_INDICATION


def main_kb(*buttons: str) -> InlineKeyboardMarkup:
    """
    Основная инлайн клавиатура
    :param buttons: ключи кнопок из LEXICON_FOR_INDICATION.
    :return: Инлайн клавиатуру с кнопками друг под другом
    """
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for button in buttons:
        kb_builder.row(InlineKeyboardButton(
            text=LEXICON_FOR_INDICATION[button] if button in LEXICON_FOR_INDICATION else
            button, callback_data=button))
    return kb_builder.as_markup()
