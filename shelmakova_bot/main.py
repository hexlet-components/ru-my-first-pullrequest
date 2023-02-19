from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib

from settings import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

NUMBER = 0

@dp.message_handler(commands=['start'])
async def cmd_command(message: types.Message) -> None:
    await message.answer(text='Введите число')


@dp.message_handler()
async def number_handler(message: types.Message) -> None:
    global NUMBER
    try:
        NUMBER = int(message.text)
    except:
        return await message.reply('Необходимо ввести число')
    await message.reply(text="Ваши данные сохранены")


@dp.inline_handler()
async def inl_mode(inline_query: types.InlineQuery) -> None:
    text = InputTextMessageContent(f"<b>{inline_query.query}</b> - {NUMBER}", parse_mode='html') or 'Echo'
    result_id = hashlib.md5(inline_query.query.encode()).hexdigest()

    item = InlineQueryResultArticle(
        input_message_content=text,
        id=result_id,
        title='This is the description'
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)