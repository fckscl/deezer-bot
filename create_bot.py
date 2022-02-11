from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import deezer

storage = MemoryStorage()

client = deezer.Client()

class Search(StatesGroup):
    track = State()
    album = State()
    artist = State()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)