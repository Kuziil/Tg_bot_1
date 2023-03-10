import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu


async def main():
    """
    Функция конфигурирования и запуска бота
    """
    # инициализация бота и диспетчера
    config: Config = load_config()
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')  # parse_mode='HTML' - поддержка HTML тегов
    dp: Dispatcher = Dispatcher()

    # инициализируем меню
    await set_main_menu(bot)

    # регистрация роутеров в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)  # пропуск накопившихся запросов
    await dp.start_polling(bot)  # запуск пулинга


if __name__ == '__main__':
    asyncio.run(main())  # запуск функции main
