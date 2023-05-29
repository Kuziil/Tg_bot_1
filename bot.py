import logging
import json
import os
import sys

from aiogram import Bot, Dispatcher, types
from handlers import main_handlers, other_handlers

from keyboards.main_menu import set_main_menu


class CustomJSONFormatter(logging.Formatter):
    """
    Этот класс позволяет записывать логи в корректной форме. Это обусловлено тем, что в yc function -> Логи ->
    есть таблица и в ней столбец урони. Если этого класса не будет, то логи не будут детектиться в этом столбце
    """

    def format(self, record):
        log_record = {
            'time': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage(),
        }
        return json.dumps(log_record)


logger = logging.getLogger()
logger.handlers.clear()  # удаляем все обработчики логов по умолчанию

handler = logging.StreamHandler(sys.stdout)
formatter = CustomJSONFormatter()
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)  # устанавливаем уровень логирования для консольного обработчика

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Создайте экземпляр бота и диспетчера, а также указываем каким образом будет происходить форматирование.
# В данном случае код распознает теги HTML
bot = Bot(os.environ.get('TOKEN'), parse_mode='HTML')
dp = Dispatcher()

# Подсоединяем роутеры. Это нужно для того чтобы хэндлеры в других файлах актировались и ловили апдейт.
dp.include_router(main_handlers.main_router)
dp.include_router(other_handlers.router)


# Functions for Yandex.Cloud
async def process_event(event):
    """
    Преобразование события функции yc в обновление и
    обработка этого обновления.
    """
    update = types.Update.parse_obj(json.loads(event['body']))
    # logging.debug('Update: ' + str(update))

    await set_main_menu(bot)
    await dp.feed_update(bot, update)


async def my_handler(event, context):
    """yc functions handler."""
    if event['httpMethod'] == 'POST':
        await process_event(event)

        return {'statusCode': 200, 'body': 'ok'}
    return {'statusCode': 405}
