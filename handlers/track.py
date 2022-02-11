from aiogram import Dispatcher, types
from create_bot import Search, bot, dp, client

#@dp.message_handler(commands='track', state=None)
async def track(message : types.Message):
    await Search.track.set()
    await bot.send_message(message.from_user.id, 'Пришли мне название желаемого трека')

#@dp.message_handler(state=Search.track, content_types='any')
async def answer_track(message : types.Message, state: Search):
    search = client.search(message.text)
    await bot.send_message(message.from_user.id, (search[0].link))
    await state.finish()

def register_handlers_track(dp : Dispatcher):
    dp.register_message_handler(track, commands='track', state=None)
    dp.register_message_handler(answer_track, state=Search.track, content_types='any')