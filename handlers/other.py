from create_bot import dp, bot
from aiogram import Dispatcher, types

async def start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Приветствую! В данном боте вы сможете найти песню, альбом или артиста в '
    'базе музыкального сервиса Deezer. Для начала работы введите нужную команду, а затем искомое слово. Удачи!')

#@dp.message_handler()
async def foo(message : types.Message):
    #await message.answer(message.text)
    #await message.reply(message.text)
    await bot.send_message(message.from_user.id, 'Что-то не сработало')

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help', 'about'])
    dp.register_message_handler(foo)
    
