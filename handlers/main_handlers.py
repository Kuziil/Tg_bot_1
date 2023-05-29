from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import LEXICON_COMMANDS, LEXICON_FOR_API
from keyboards.keyboards_start import main_kb
from keyboards.keyboards_for_students import main_students_kb
from handlers import student_handlers, employee_handlers
from resources.API import response

main_router: Router = Router()
main_router.include_router(student_handlers.student_router)
main_router.include_router(employee_handlers.employee_router)


@main_router.message(CommandStart())
async def process_start_command(message: Message):
    """
    Этот хэндлер срабатывает при отправке пользователем команды /start.
    Ответ пользователя обрабатывается в employee_handlers.py или в student_handlers.py
    в зависимости от выбора пользователя.
    :return: Предлагает сделать выбор, кем вы являетесь в вузе, через инлайн кнопки
    """
    await message.answer(text=LEXICON_COMMANDS['/start'],
                         reply_markup=main_kb(
                             'student', 'employee', 'test_api'
                         ))


@main_router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    """
    Этот хэндлер срабатывает при отправке пользователем команды /help.
    :param message:
    :return: LEXICON['/help']
    """
    await message.answer(text=LEXICON_COMMANDS['/help'])


@main_router.callback_query(Text(text=['back_after_start_for_students']))
async def process_back_command(callback: CallbackQuery):
    """
    Этот хэндлер возвращает /start
    :param callback:
    :return:
    """
    await callback.message.edit_text(text=LEXICON_COMMANDS['/start'],
                                     reply_markup=main_kb(
                                         'student', 'employee', 'test_api'
                                     ))


@main_router.callback_query(
    lambda x: True if x.data == 'back_after_certificates_for_students' or x.data == 'test_api' else False)
async def process_api_press(callback: CallbackQuery):
    """
    Этот хэндлер срабатывает при нажатии кнопки 'Овощи?' и обрабатывает этот запрос.
    Также является обработчиком кнопки назад.
    :return: Возвращает новые кнопки заменяя текст над сообщением и новые кнопки
    """
    await callback.message.edit_text(
        text=LEXICON_FOR_API['after_start_for_api'],
        reply_markup=main_students_kb(*[response[x]['name'] for x in range(len(response))])
    )
