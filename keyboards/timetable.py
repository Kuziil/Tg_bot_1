import calendar
from datetime import datetime

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def timetable_kb(year: int = datetime.now().year,
                 month: int = datetime.now().month) -> InlineKeyboardMarkup:
    ignore_callback = 'IGNORE'
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(InlineKeyboardButton(text='<<', callback_data='backward_for_tb'),
                   InlineKeyboardButton(text=f'{calendar.month_name[month]} {str(year)}',
                                        callback_data=ignore_callback),
                   InlineKeyboardButton(text='>>', callback_data='forward_for_tb'))
    kb_builder.row(*[InlineKeyboardButton(text=day, callback_data=ignore_callback) for day in
                     ["Пн", "Вт", "Ср", "Чт", "Пт", "Су", "Вс"]])
    month_calendar = calendar.monthcalendar(year, month)
    buttons: list[InlineKeyboardButton] = []
    for week in month_calendar:
        for day in week:
            if day == 0:
                buttons.append(InlineKeyboardButton(text=" ", callback_data=ignore_callback))
                continue
            buttons.append(InlineKeyboardButton(
                text=str(day), callback_data=str(day) + '_timetable'
            ))
    kb_builder.row(*buttons, width=7)
    return kb_builder.as_markup()
