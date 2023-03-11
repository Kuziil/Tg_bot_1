import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import main_handlers, other_handlers
from keyboards.main_menu import set_main_menu

logger = logging.getLogger(__name__)


async def main():
    """
    Функция конфигурирования и запуска бота
    """
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # инициализация бота и диспетчера
    config: Config = load_config()
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')  # parse_mode='HTML' - поддержка HTML тегов
    dp: Dispatcher = Dispatcher()

    # инициализируем меню
    await set_main_menu(bot)

    # регистрация роутеров в диспетчере
    dp.include_router(main_handlers.main_router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)  # пропуск накопившихся запросов
    await dp.start_polling(bot)  # запуск пулинга


if __name__ == '__main__':
    asyncio.run(main())  # запуск функции main
