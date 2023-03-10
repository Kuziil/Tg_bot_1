from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon import LEXICON_COMMANDS_FOR_MENU


async def set_main_menu(bot: Bot):
    """
    Функция создания меню.
    Берет значения из lexicon.lexicon.LEXICON_COMMANDS_FOR_MENU
    """
    main_menu_commands = [BotCommand(command=command, description=description)
                          for command, description in LEXICON_COMMANDS_FOR_MENU.items()]
    await bot.set_my_commands(main_menu_commands)
