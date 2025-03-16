import asyncio
import logging
from catboost import CatBoostClassifier
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import pandas as pd


from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode


class Form(StatesGroup):
    Gender = State()  # Ожидание ответа на первый вопрос
    Age = State()  # Ожидание ответа на второй вопрос
    Weight = State()
    Height = State()
    family_history = State()
    FAVC = State()
    FCVC = State()
    NCP = State()
    CAEC = State()
    SMOKE = State()
    CH2O = State()
    SCC = State()
    FAF = State()
    TUE = State()
    CALC = State()
    MTRANS = State()



button_start = KeyboardButton(text='Начать')
button1 = KeyboardButton(text='0')
button2 = KeyboardButton(text='1')
start_kb = ReplyKeyboardMarkup(keyboard=[[button_start], []], resize_keyboard=True)
binary_kb = ReplyKeyboardMarkup(keyboard=[[button1,button2]], resize_keyboard=True)


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="")
# Диспетчер
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("👋 Привет! Этот бот поможет тебе понять, в какой группе риска лишнего веса ты находишься. Нажми Начать, что бы начать", reply_markup=start_kb)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


@dp.message(F.text.lower() == "начать")
async def smook_handler(msg: Message, state: FSMContext, ):
    await msg.answer('Укажите ваш пол', reply_markup=binary_kb)
    await state.set_state(Form.Gender)


@dp.message(Form.Gender)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(Gender = msg.text)
    await msg.answer('Укажите ваш возраст')
    await state.set_state(Form.Age)

@dp.message(Form.Age)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(Age = msg.text)
    await msg.answer('Укажите ваш рост')
    await state.set_state(Form.Height)

@dp.message(Form.Height)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(Height = msg.text)
    await msg.answer('Укажите ваш вес')
    await state.set_state(Form.Weight)

@dp.message(Form.Weight)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(Weight = msg.text)
    await msg.answer('Ваши родственники страдали от лишнего веса?', reply_markup=binary_kb)
    await state.set_state(Form.family_history)

@dp.message(Form.family_history)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(family_history = msg.text)
    await msg.answer('Питаетесь ли вы фастфудом?', reply_markup=binary_kb)
    await state.set_state(Form.FAVC)

@dp.message(Form.FAVC)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(FAVC = msg.text)
    await msg.answer('Как часто вы питаетесь овощами?')
    await state.set_state(Form.FCVC)

@dp.message(Form.FCVC)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(FCVC = msg.text)
    await msg.answer('Ввидите количество основных приемов пищи')
    await state.set_state(Form.NCP)

@dp.message(Form.NCP)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(NCP = msg.text)
    await msg.answer('Делаете ли вы перекусы между приемами пищи. Отвечайте в следующем порядке: "нет : 0", "иногда : 1", "часто : 2", "постояно : 3"')
    await state.set_state(Form.CAEC)

@dp.message(Form.CAEC)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(CAEC = msg.text)
    await msg.answer('Курите ли вы?')
    await state.set_state(Form.SMOKE)

@dp.message(Form.SMOKE)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(SMOKE = msg.text)
    await msg.answer('Сколько литров воды в среднем пьете в день?')
    await state.set_state(Form.CH2O)

@dp.message(Form.CH2O)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(CH2O = msg.text)
    await msg.answer('Ведете ли вы подсчет каллорий которые потребляете?', reply_markup=binary_kb)
    await state.set_state(Form.SCC)

@dp.message(Form.SCC)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(SCC = msg.text)
    await msg.answer('Как часто вы занимаетесь физической активностью?')
    await state.set_state(Form.FAF)

@dp.message(Form.FAF)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(FAF = msg.text)
    await msg.answer('Как часто вы пользуетесь технологическими устройствами?(от 0 до 2, где 0 не пользуюсь, 2 пользуюсь ежечасно)')
    await state.set_state(Form.TUE)

@dp.message(Form.TUE)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(TUE = msg.text)
    await msg.answer('Часто ли вы пьюте алкогольниые напитки? Отвечайте в следующем порядке: "нет : 0", "иногда : 1", "часто : 2", "постояно : 3"')
    await state.set_state(Form.CALC)

@dp.message(Form.CALC)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(CALC = msg.text)
    await msg.answer('Каким способом передвижения вы пользуетесь чаще всего? Отвечайте в следующем порядке: "Общественный транспорт : 0", "Передвигаюсь пешком : 1", "Автомобиль : 2", "Мотоцикл : 3", "Велосипед : 4"')
    await state.set_state(Form.MTRANS)

@dp.message(Form.MTRANS)
async def smook_handler(msg: Message, state: FSMContext):
    await state.update_data(MTRANS = msg.text)
    # Получаем все сохраненные данные
    data = await state.get_data()

    predict_data = pd.DataFrame([data])

    model = CatBoostClassifier()
    model.load_model('best_catboost_model.cbm')

    prob = model.predict(predict_data)
    obesity_dict = {0 : 'Нормальный все', 1: 'избыточный вес I степени', 2 : 'избыточный вес II степени',
       3 : 'Ожирение I степени', 4 : 'Недостаточный вес', 5: 'Ожирение II степени',
       6 : 'Ожирение III степени'}
    # Отправляем пользователю его ответы
    await msg.answer(f"Ваш результат: {obesity_dict[prob[0][0]]}")

    # Сбрасываем состояние
    await state.clear()



if __name__ == "__main__":
    asyncio.run(main())

