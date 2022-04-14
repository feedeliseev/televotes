from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from votesdb import voter, spectate_vote
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from admin_data import token, admin_id
from datetime import datetime


bot = Bot(token=token)



dp = Dispatcher(bot, storage=MemoryStorage())



class state(StatesGroup):
    state1 = State()
    state2 = State()

@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await message.answer(text='Привет, введи /help')
    await bot.send_message(chat_id=admin_id, text=f'Пользователь с id {message.chat.id} начал работу с ботом')

@dp.message_handler(commands='help')
async def help_message(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo='https://sun9-39.userapi.com/impg/c854320/v854320881/1edab0/RxonPZMWyCQ.jpg?size=810x1080&quality=96&sign=0efc854b00caa8090a00d668094ab5c6&type=album')
    await message.answer(text='Это бот для голосование за участников события, которые произойдут в субботу.\nЕсли хотите проголосовать, то введите комманду /vote')

@dp.message_handler(commands='vote')
async def vote0_message(message: types.Message):
    await message.answer('Напишите 1, если хотите проголосовать за Ивана.\nНапишите 2, если хотите проголосовать за Фарида.\nГолос отменить или изменить нельзя')
    await state.state1.set()

@dp.message_handler(text='1', state = state.state1)
async def vote1_message(message: types.Message):
    await message.answer('Спасибо за выбор Ивана.')
    await message.answer('Теперь вы наблюдатель. /watch')
    tgvoter = voter(int(message.chat.id), 1, 0)
    tgvoter.add_vote()
    await state.state2.set()

@dp.message_handler(text='2', state = state.state1)
async def vote1_message(message: types.Message):
    await message.answer('Спасибо за выбор Фарида.')
    await message.answer('Теперь вы наблюдатель. /watch')
    tgvoter = voter(int(message.chat.id), 0, 1)
    tgvoter.add_vote()
    await state.state2.set()

@dp.message_handler(commands='vote', state = state.state2)
async def non_vote_message(message: types.Message):
    await message.answer('Вы уже проголосовали!')

@dp.message_handler(commands='help', state = state.state2)
async def help_non_vote_message(message: types.Message):
    await message.answer('Вы уже проголосовали. Хотите понаблюдать за результатами? - /watch')

@dp.message_handler(commands='start', state = state.state2)
async def start_message(message: types.Message):
    await message.answer(text='Привет, введи /help')

@dp.message_handler(commands='watch', state= state.state2)
async def spectate_message(message: types.Message):
    ivan_votes, farid_votes = spectate_vote()
    await message.answer(text=f'За Ивана проголосовало {ivan_votes} человек, а за Фарида проголосовало {farid_votes} человек.\nАктуально на {str(datetime.now())}')


executor.start_polling(dp)
