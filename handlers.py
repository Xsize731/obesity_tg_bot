from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode


router = Router()

button_start = KeyboardButton(text='Приступим')
button1 = KeyboardButton(text='1')
button2 = KeyboardButton(text='2')
start_kb = ReplyKeyboardMarkup(keyboard=[[button_start], []], resize_keyboard=True)
binary_kb = ReplyKeyboardMarkup(keyboard=[[button1], [button2]], resize_keyboard=True)

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("👋 Привет! Этот бот поможет тебе понять, в какой группе риска лишнего веса ты находишься. Нажми Начать, что бы начать", reply_markup=start_kb)


@router.message(Command("Приступим"))
async def message_handler(msg: Message):
    await msg.answer('Курите ли Вы?', reply_markup=binary_kb)