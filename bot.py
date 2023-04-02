import logging
import json
import os

from aiogram import Bot, Dispatcher, types
from handlers import main_handlers, other_handlers

from keyboards.main_menu import set_main_menu

# Logger initialization and logging level setting
log = logging.getLogger(__name__)
log.setLevel(os.environ.get('LOGGING_LEVEL', 'INFO').upper())

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
    log.debug('Update: ' + str(update))

    await set_main_menu(bot)
    await dp.feed_update(bot, update)


async def handler(event, context):
    """Yandex.Cloud functions handler."""
    log.debug('ev method:' + str(event['httpMethod']))
    if event['httpMethod'] == 'POST':
        await process_event(event)

        return {'statusCode': 200, 'body': 'ok'}
    return {'statusCode': 405}
