from aiogram import Dispatcher, types
from create_bot import Search, bot, dp, client

#@dp.message_handler(commands='track', state=None)
async def album(message : types.Message):
    await Search.album.set()
    await bot.send_message(message.from_user.id, 'Пришли мне название желаемого альбома')

#@dp.message_handler(state=Search.track, content_types='any')
async def answer_album(message : types.Message, state: Search):
    search = client.search(message.text)
    await bot.send_message(message.from_user.id, search[0].get_album().link)
    await state.finish()

def register_handlers_album(dp : Dispatcher):
    dp.register_message_handler(album, commands='album', state=None)
    dp.register_message_handler(answer_album, state=Search.album, content_types='any')
