import logging
import json
import os
import sys

from aiogram import Bot, Dispatcher, types
from handlers import main_handlers, other_handlers

from keyboards.main_menu import set_main_menu


class CustomJSONFormatter(logging.Formatter):
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

# Create an instance of the Bot and Dispatcher
bot = Bot(os.environ.get('TOKEN'))
dp = Dispatcher()

dp.include_router(main_handlers.main_router)
dp.include_router(other_handlers.router)


# Functions for Yandex.Cloud
async def process_event(event):
    """
    Converting an Yandex.Cloud functions event to an update and
    handling tha update.
    """
    update = types.Update.parse_obj(json.loads(event['body']))
    # log.debug('Update: ' + str(update))
    logging.info('Hellооооo')

    await set_main_menu(bot)
    await dp.feed_update(bot, update)


async def my_handler(event, context):
    """Yandex.Cloud functions handler."""
    logging.debug('helo2222')
    if event['httpMethod'] == 'POST':
        await process_event(event)

        return {'statusCode': 200, 'body': 'ok'}
    return {'statusCode': 405}
