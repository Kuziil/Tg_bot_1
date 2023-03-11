from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_FOR_INDICATION


def user_identifier(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON_FOR_INDICATION[button] if button in LEXICON_FOR_INDICATION else
        button, callback_data=button)
        for button in buttons])
    return kb_builder.as_markup()
