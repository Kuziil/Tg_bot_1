from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Привет!')
