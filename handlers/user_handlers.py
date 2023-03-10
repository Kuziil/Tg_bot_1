from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from lexicon.lexicon import LEXICON_COMMANDS

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """
    Этот хэндлер срабатывает при отправке пользователем команды /start.
    :param message:
    :return: LEXICON_COMMANDS['/start']
    """
    await message.answer(text=LEXICON_COMMANDS['/start'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    """
    Этот хэндлер срабатывает при отправке пользователем команды /help.
    :param message:
    :return: LEXICON['/help']
    """
    await message.answer(text=LEXICON_COMMANDS['/help'])
