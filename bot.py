import asyncio
import json
import os

from aiogram import Bot, Dispatcher, types
from handlers import main_handlers, other_handlers
from keyboards.main_menu import set_main_menu


async def main(update):
    # инициализация бота и диспетчера
    bot: Bot = Bot(token=os.environ.get('TOKEN'),
                   parse_mode='HTML')  # parse_mode='HTML' - поддержка HTML тегов
    dp: Dispatcher = Dispatcher()

    await set_main_menu(bot)

    # регистрация роутеров в диспетчере
    dp.include_router(main_handlers.main_router)
    dp.include_router(other_handlers.router)

    await dp.feed_update(bot=bot, update=update)


def starting_point(event, _):
    update = json.loads(event['body'])
    update = types.Update.parse_obj(update)
    asyncio.run(main(update))  # запуск функции main
    return {
        'statusCode': 200,
        'body': '!',
    }
