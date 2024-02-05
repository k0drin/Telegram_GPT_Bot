from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from config import gpt
    
TOKEN = 'YOUR BOT TOKEN'      
bot = Bot(TOKEN)
dp = Dispatcher(bot)
    

@dp.message_handler(commands='start')           
async def start(message: Message):
    await message.answer('Вітаю👋, це твій персональний ШІ🤖 \nще питання❓')


@dp.message_handler(content_types=types.ContentType.TEXT) # Request to chatgpt. 
async def mes(message: types.Message): 
    await message.answer('Я думаю🤔, почекай')            
    await message.reply(gpt(message.text)) # type: ignore Here the request is accepted, processed and output
    
if __name__ == '__main__': 
    executor.start_polling(dp)
