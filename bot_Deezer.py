from aiogram.utils import executor
from create_bot import dp
from handlers import track, album, artist, other

track.register_handlers_track(dp)
album.register_handlers_album(dp)
artist.register_handlers_artist(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True)