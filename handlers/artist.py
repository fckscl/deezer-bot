from aiogram import Dispatcher, types
from create_bot import Search, bot, dp, client

#@dp.message_handler(commands='track', state=None)
async def artist(message : types.Message):
    await Search.artist.set()
    await bot.send_message(message.from_user.id, 'Пришли мне название желаемого исполнителя')

#@dp.message_handler(state=Search.track, content_types='any')
async def answer_artist(message : types.Message, state: Search):
    search = client.search(message.text)
    await bot.send_message(message.from_user.id, (search[0].get_artist().link))
    await state.finish()

def register_handlers_artist(dp : Dispatcher):
    dp.register_message_handler(artist, commands='artist', state=None)
    dp.register_message_handler(answer_artist, state=Search.artist, content_types='any')
